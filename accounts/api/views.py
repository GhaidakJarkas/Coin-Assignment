from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

from accounts.api.serializers import CustomUserSerializer



@api_view(['POST'])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["POST"])
def log_in(request):
    email = request.data['email'].lower()
    password = request.data['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
        return Response(data=tokens, status=status.HTTP_200_OK)
    return Response({"message": "Email or Password is incorrect"}, status=status.HTTP_403_FORBIDDEN)