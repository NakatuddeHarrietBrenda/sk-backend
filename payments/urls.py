# from django.urls import path
# from .views import pay, mtn_callback, airtel_callback
# from .views import dashboard_stats

# urlpatterns = [
#     path("pay/", pay),
#     path("mtn-callback/", mtn_callback),
#     path("airtel-callback/", airtel_callback),
#      path("dashboard-stats/", dashboard_stats),
# ]


from django.urls import path
from .views import pay, receipt, mtn_callback, airtel_callback, user_payments

urlpatterns = [
    path("pay/", pay), # This becomes /api/payments/pay/
    path("receipt/<str:transaction_id>/", receipt),
    path("user-payments/<int:user_id>/", user_payments),

    path("mtn-callback/", mtn_callback),
    path("airtel-callback/", airtel_callback),
]