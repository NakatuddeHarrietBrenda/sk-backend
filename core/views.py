from django.db.models import Count
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from properties.models import Property
from users.models import User
from payments.models import Payment

@staff_member_required
def admin_dashboard(request):

    property_counts = Property.objects.values('location').annotate(total=Count('id'))

    context = {
        "total_properties": Property.objects.count(),
        "total_users": User.objects.count(),
        "total_payments": Payment.objects.count(),

        "labels": [p["location"] for p in property_counts],
        "data": [p["total"] for p in property_counts],
    }

    return render(request, "admin/dashboard.html", context)