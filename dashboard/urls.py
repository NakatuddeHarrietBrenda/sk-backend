from django.urls import path
from .views import dashboard_stats, recent_payments

urlpatterns = [
    path("stats/", dashboard_stats),
    path("recent-payments/", recent_payments),
]