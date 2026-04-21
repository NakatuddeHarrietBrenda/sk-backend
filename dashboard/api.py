from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from payments.models import Payment
from properties.models import Property
from users.models import User


# 📊 MAIN STATS API
@staff_member_required
def dashboard_stats(request):
    return JsonResponse({
        "total_users": User.objects.count(),
        "total_properties": Property.objects.count(),
        "total_payments": Payment.objects.count(),
        "pending_payments": Payment.objects.filter(status="pending").count(),
        "successful_payments": Payment.objects.filter(status="success").count(),
    })


# 💳 RECENT PAYMENTS
@staff_member_required
def recent_payments(request):
    payments = Payment.objects.order_by("-created_at")[:10]

    data = [
        {
            "id": p.id,
            "user": p.user.username,
            "amount": float(p.amount),
            "method": p.method,
            "status": p.status,
            "phone": p.phone_number,
            "date": p.created_at,
        }
        for p in payments
    ]

    return JsonResponse(data, safe=False)