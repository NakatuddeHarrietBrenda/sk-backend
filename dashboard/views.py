from django.http import JsonResponse
from payments.models import Payment
from properties.models import Property
from users.models import User

def dashboard_stats(request):
    return JsonResponse({
        "total_users": User.objects.count(),
        "total_properties": Property.objects.count(),
        "total_payments": Payment.objects.count(),
        "pending_payments": Payment.objects.filter(status="pending").count(),
        "successful_payments": Payment.objects.filter(status="success").count(),
    })


def recent_payments(request):
    payments = Payment.objects.order_by("-created_at")[:10]
    data = list(payments.values())
    return JsonResponse(data, safe=False)