from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
import json

from .models import Payment
from .services.mtn import request_to_pay
from .services.airtel import request_airtel_payment
from .receipts import generate_receipt # Import your new function


# =========================
# 💳 INITIATE PAYMENT (MTN / AIRTEL)
# =========================
@csrf_exempt
def pay(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    try:
        data = json.loads(request.body)

        phone = data.get("phone")
        amount = data.get("amount")
        network = data.get("network")  # MTN or Airtel
        user_id = data.get("user_id", 1)
        property_id = data.get("property_id", 1)

        if not phone or not amount or not network:
            return JsonResponse({"error": "Missing fields"}, status=400)

        # Create payment record
        payment = Payment.objects.create(
            user_id=user_id,
            property_id=property_id,
            amount=amount,
            method=network,
            status="pending",
            phone_number=phone
        )

        # =========================
        # MTN PAYMENT
        # =========================
        if network == "MTN":
            ref, status, resp = request_to_pay(phone, amount)

        # =========================
        # AIRTEL PAYMENT
        # =========================
        elif network == "AIRTEL":
            ref, status, resp = request_airtel_payment(phone, amount)

        else:
            return JsonResponse({"error": "Invalid network"}, status=400)

        payment.transaction_id = ref
        payment.save()

        return JsonResponse({
            "message": "Payment initiated",
            "payment_id": payment.id,
            "reference": ref,
            "gateway_status": status
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# =========================
# 🔵 MTN CALLBACK
# =========================
@csrf_exempt
def mtn_callback(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        ref = data.get("externalId")
        status = data.get("status", "SUCCESS")

        Payment.objects.filter(transaction_id=ref).update(
            status="success" if status == "SUCCESS" else "failed"
        )

        return JsonResponse({"message": "MTN callback received"})


# =========================
# 🟠 AIRTEL CALLBACK
# =========================
@csrf_exempt
def airtel_callback(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        ref = data.get("reference")
        status = data.get("status", "SUCCESS")

        Payment.objects.filter(transaction_id=ref).update(
            status="success" if status == "SUCCESS" else "failed"
        )

        return JsonResponse({"message": "Airtel callback received"})


# =========================
# 📊 DASHBOARD STATS
# =========================
def dashboard_stats(request):
    total = Payment.objects.count()

    revenue = Payment.objects.filter(status="success").aggregate(
        total=Sum("amount")
    )["total"] or 0

    return JsonResponse({
        "total_payments": total,
        "revenue": float(revenue)
    })



def receipt(request, transaction_id):
    try:
        payment = Payment.objects.get(transaction_id=transaction_id)
        
        # Generate the PDF and get the URL
        pdf_url = generate_receipt(payment)

        return JsonResponse({
            "transaction_id": payment.transaction_id,
            "amount": payment.amount,
            "phone_number": payment.phone_number,
            "method": payment.method,
            "status": payment.status,
            "pdf_url": request.build_absolute_uri(pdf_url) # Send full URL to React
        })

    except Payment.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)