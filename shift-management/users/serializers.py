from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(write_only=True, min_length = 8)

    first_name = serializers.CharField(max_length=30, required=True, allow_blank = False)
    last_name = serializers.CharField(max_length=30, required=True, allow_blank = False)

    role = serializers.ChoiceField(choices=[("nurse", "nurse"), ("head_nurse", "head_nurse")])

    def validate_username(self, v):
        if User.objects.filter(username=v).exists():
            raise serializers.ValidationError("Username already exists.")
        return v
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name = validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        UserProfile.objects.create(user=user, role =validated_data["role"])
        return user
        
class MeSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    nurse_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "nurse_id", "role"]
    def get_role(self, obj):
        return getattr(getattr(obj, "profile", None), "role", None)
    def get_nurse_id (self, obj):
        return getattr(getattr(obj, "profile", None), "nurse_id", None)
