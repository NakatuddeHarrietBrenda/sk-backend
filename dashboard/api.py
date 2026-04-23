from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from payments.models import Payment
from properties.models import Property
from users.models import User
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth


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


# 🏠 PROPERTIES BY TYPE API
@staff_member_required
def properties_by_type(request):
    data = Property.objects.values("property_type").annotate(count=Count("id"))
    return JsonResponse(list(data), safe=False)


# 💰 REVENUE BY MONTH API
@staff_member_required
def revenue_by_month(request):
    data = Payment.objects.filter(status="success") \
        .annotate(month=TruncMonth("created_at")) \
        .values("month") \
        .annotate(total=Sum("amount")) \
        .order_by("month")
    
    formatted_data = [
        {"month": item["month"].strftime("%b %Y"), "total": float(item["total"])}
        for item in data
    ]
    return JsonResponse(formatted_data, safe=False)


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
            "date": p.created_at.strftime("%Y-%m-%d %H:%M"),
        }
        for p in payments
    ]

    return JsonResponse(data, safe=False)