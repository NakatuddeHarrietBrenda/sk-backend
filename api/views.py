import requests
import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Property, Contact, Payment
from .serializers import PropertySerializer, ContactSerializer, PaymentSerializer


# GET PROPERTIES

@api_view(['GET'])
def properties(request):

    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)

    return Response(serializer.data)



# CONTACT FORM

@api_view(['POST'])
def contact(request):

    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Message sent successfully"})

    return Response(serializer.errors)



# PAYMENT VIEW (MTN / AIRTEL)

@api_view(['POST'])
def make_payment(request):

    amount = request.data['amount']
    phone = request.data['phone_number']
    network = request.data['network']

    tx_ref = str(uuid.uuid4())

    payment = Payment.objects.create(
        tx_ref=tx_ref,
        amount=amount,
        phone_number=phone,
        network=network
    )

    url = "https://api.flutterwave.com/v3/charges?type=mobile_money_uganda"

    payload = {
        "tx_ref": tx_ref,
        "amount": amount,
        "currency": "UGX",
        "network": network,
        "email": "customer@email.com",
        "phone_number": phone
    }

    headers = {
        "Authorization": "Bearer YOUR_SECRET_KEY"
    }

    response = requests.post(url, json=payload, headers=headers)

    return Response(response.json())