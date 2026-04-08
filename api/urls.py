from django.urls import path
from . import views


urlpatterns = [

path('properties/', views.properties),

path('contact/', views.contact),

path('payments/', views.make_payment),

]