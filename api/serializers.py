from rest_framework import serializers
from .models import Property, Contact, Payment


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'