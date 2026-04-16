from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact

@csrf_exempt
def send_message(request):
    data = json.loads(request.body)

    Contact.objects.create(
        name=data["name"],
        email=data["email"],
        message=data["message"]
    )

    return JsonResponse({"message": "Message sent"})