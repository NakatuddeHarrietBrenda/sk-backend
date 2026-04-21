from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Contact

@api_view(['POST'])
def send_message(request):
    Contact.objects.create(
        name=request.data.get("name"),
        email=request.data.get("email"),
        message=request.data.get("message")
    )

    return Response({"message": "Message sent"})