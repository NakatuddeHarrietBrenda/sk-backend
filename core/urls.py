from django.urls import path
from .views import (
    admin_dashboard,
    dashboard_stats,
    recent_payments,
    approve_payment,
    reject_payment,
    download_receipt
)

urlpatterns = [
    path("dashboard/", admin_dashboard),
    path("dashboard-stats/", dashboard_stats),
    path("recent-payments/", recent_payments),

    # 🔥 NEW ACTION ROUTES
    path("payment/<int:payment_id>/approve/", approve_payment),
    path("payment/<int:payment_id>/reject/", reject_payment),
    path("payment/<int:payment_id>/receipt/", download_receipt),
]