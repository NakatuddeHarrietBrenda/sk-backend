from django.db import models
from users.models import User
from properties.models import Property


class Payment(models.Model):

    PAYMENT_METHODS = [
        ("MTN", "MTN"),
        ("AIRTEL", "AIRTEL"),
    ]

    STATUS = [
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    ]

    # 🔥 REAL RELATIONSHIPS (IMPORTANT FIX)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=12, decimal_places=2)

    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)

    status = models.CharField(
        max_length=20,
        default="pending",
        choices=STATUS
    )

    phone_number = models.CharField(max_length=20)

    # 🔥 MTN / Airtel reference
    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.method}"