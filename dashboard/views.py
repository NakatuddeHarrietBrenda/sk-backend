from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum

from payments.models import Payment
from properties.models import Property
from users.models import User


# =========================
# 🧠 ADMIN DASHBOARD PAGE (HTML)
# =========================
@staff_member_required
def admin_dashboard(request):

    context = {
        "total_users": User.objects.count(),
        "total_properties": Property.objects.count(),
        "total_payments": Payment.objects.count(),
        "total_messages": 0,  # replace if you track contacts

        "revenue": Payment.objects.filter(status="success").aggregate(
            total=Sum("amount")
        )["total"] or 0,
    }

    return render(request, "admin/dashboard.html", context)


# =========================
# 📊 DASHBOARD API (FOR CHARTS)
# =========================
def dashboard_stats(request):

    return JsonResponse({
        "total_users": User.objects.count(),
        "total_properties": Property.objects.count(),
        "total_payments": Payment.objects.count(),
        "pending_payments": Payment.objects.filter(status="pending").count(),
        "successful_payments": Payment.objects.filter(status="success").count(),
    })


# =========================
# 💳 RECENT PAYMENTS FEED
# =========================
def recent_payments(request):

    payments = Payment.objects.order_by("-created_at")[:10]

    data = list(payments.values(
        "id",
        "amount",
        "method",
        "status",
        "created_at",
        "phone_number"
    ))

    return JsonResponse(data, safe=False)


# from django.contrib.admin.views.decorators import staff_member_required
# from django.shortcuts import render
# from payments.models import Payment
# from properties.models import Property
# from users.models import User
# from django.db.models import Sum


# @staff_member_required
# def admin_dashboard(request):

#     context = {
#         "users": User.objects.count(),
#         "properties": Property.objects.count(),
#         "payments": Payment.objects.count(),
#         "revenue": Payment.objects.filter(status="success").aggregate(
#             total=Sum("amount")
#         )["total"] or 0,
#     }

#     return render(request, "admin/dashboard.html", context)