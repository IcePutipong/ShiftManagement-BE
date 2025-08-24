from django.shortcuts import render
from rest_framework import status, generics, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import RegisterSerializer, MeSerializer
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class RegisterUserView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    def post(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        nurse_id = getattr(getattr(user, "profile", None), "nurse_id", None)
        return Response({"nurse_id": nurse_id, "username": user.username}, status=status.HTTP_201_CREATED)
    
class ProfileDataView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MeSerializer
    def get_object(self):
        return self.request.user
    
class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["role"] = getattr(getattr(user , "profile", None), "role", None)
        return token
    def validate(self, attrs):
        data = super().validate(attrs)
        data["role"] = getattr(getattr(self.user, "profile", None), "role", None)
        return data
    
class LoginUserView(TokenObtainPairView):
    serializer_class =  UserTokenObtainPairSerializer

class LogoutUserView(APIView):
    permission_classes= [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

