from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "location",
        "property_type",
        "created_at"
    )

    list_filter = ("property_type", "location")
    search_fields = ("title", "location")