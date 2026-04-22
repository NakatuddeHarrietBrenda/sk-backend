from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
def register(request):
    try:
        user = User.objects.create_user(
            username=request.data.get("username"),
            email=request.data.get("email"),
            password=request.data.get("password"),
            phone_number=request.data.get("phone"), # Ensure this matches your User model
        )

        return Response({
            "message": "User created",
            "user": {
                "id": user.id,
                "username": user.username
            }
        })
    except Exception as e:
        return Response({"error": str(e)}, status=400)