from django.db import models

class Property(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to="properties/")

    def __str__(self):
        return self.title



class Contact(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name



class Payment(models.Model):

    tx_ref = models.CharField(max_length=200)
    amount = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    network = models.CharField(max_length=20)

    STATUS = (
        ('pending','Pending'),
        ('successful','Successful'),
        ('failed','Failed')
    )

    status = models.CharField(max_length=20, choices=STATUS, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tx_ref