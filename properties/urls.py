from django.urls import path
from .views import PropertyListCreateView, PropertyDetailView

urlpatterns = [
    path("properties/", PropertyListCreateView.as_view()),
    path("properties/<int:pk>/", PropertyDetailView.as_view()),
]