from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(write_only=True, min_lenght = 8)

    first_name = serializers.CharField(max_lenght=30, required=True, allow_blank = False)
    last_name = serializers.CharField(max_lenght=30, required=True, allow_blank = False)

    role = serializers.ChoiceField(choices=[("nurse", "nurse"), ("head_nurse", "head_nurse")])

    def validate_username(self, v):
        if User.objects.filter(username=v).exists():
            raise serializers.ValidationError("Username already exists.")
        return v
    
    def create(self, validate_data):
        user = User.objects.create_user(
            username=validate_data["username"],
            email=validate_data["email"],
            password=validate_data["password"],
            first_name = validate_data["first_name"],
            last_name=validate_data["last_name"],
        )
        UserProfile.objects.create(user=user, role =validate_data["role"])
        return user
        
