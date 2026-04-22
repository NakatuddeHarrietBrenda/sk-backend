from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = [
        ("HOUSE", "House"),
        ("APARTMENT", "Apartment"),
        ("LAND", "Land"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=200)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    image = models.ImageField(upload_to="properties/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
