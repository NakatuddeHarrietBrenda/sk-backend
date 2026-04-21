from django.http import JsonResponse, FileResponse
from payments.models import Payment
from payments.receipts import generate_receipt


# =========================
# ✅ APPROVE PAYMENT
# =========================
def approve_payment(request, payment_id):
    Payment.objects.filter(id=payment_id).update(status="success")
    return JsonResponse({"message": "approved"})


# =========================
# ❌ REJECT PAYMENT
# =========================
def reject_payment(request, payment_id):
    Payment.objects.filter(id=payment_id).update(status="failed")
    return JsonResponse({"message": "rejected"})


# =========================
# 📄 DOWNLOAD RECEIPT
# =========================
def download_receipt(request, payment_id):

    payment = Payment.objects.get(id=payment_id)

    file_path = generate_receipt(payment)

    return FileResponse(
        open(file_path, "rb"),
        as_attachment=True,
        filename=f"receipt_{payment.id}.pdf"
    )




# # from django.db.models import Count
# # from django.contrib.admin.views.decorators import staff_member_required
# # from django.shortcuts import render

# # from properties.models import Property
# # from users.models import User
# # from payments.models import Payment

# # @staff_member_required
# # def admin_dashboard(request):

# #     property_counts = Property.objects.values('location').annotate(total=Count('id'))

#     context = {
#         "total_properties": Property.objects.count(),
#         "total_users": User.objects.count(),
#         "total_payments": Payment.objects.count(),

#         "labels": [p["location"] for p in property_counts],
#         "data": [p["total"] for p in property_counts],
#     }

#     return render(request, "admin/dashboard.html", context)