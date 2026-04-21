# from django.urls import path
# from .views import dashboard_stats, recent_payments

# urlpatterns = [
#     path("stats/", dashboard_stats),
#     path("recent-payments/", recent_payments),
    
# ]

from django.urls import path
from .views import admin_dashboard
from .api import dashboard_stats, recent_payments

urlpatterns = [
    path("", admin_dashboard, name="dashboard"),
    path("stats/", dashboard_stats),
    path("recent-payments/", recent_payments),
]