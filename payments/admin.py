from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "property",
        "amount",
        "method",
        "status",
        "phone_number",
        "created_at"
    )

    list_filter = ("status", "method", "created_at")
    search_fields = ("user__username", "phone_number", "transaction_id")

    ordering = ("-created_at",)