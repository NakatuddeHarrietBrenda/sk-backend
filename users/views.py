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
            phone=request.data.get("phone"), # Fixed field name to 'phone'
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

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "phone": user.phone,
                "role": user.role
            }
        })
    
    return Response({"error": "Invalid credentials"}, status=401)