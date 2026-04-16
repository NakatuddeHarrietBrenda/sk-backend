from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyDetailView(generics.RetrieveDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer