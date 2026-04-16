from django.urls import path
from .views import send_message

urlpatterns = [
    path("contact/", send_message),
]