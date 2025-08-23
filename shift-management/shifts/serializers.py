from rest_framework import serializers
from .models import Shift, ShiftAssignment
from django.contrib.auth import get_user_model

User = get_user_model()


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ["id", "date", "start_time", "end_time"]

class ShiftAssignmentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    shift = serializers.PrimaryKeyRelatedField(queryset=Shift.objects.all())

    class Meta:
        model = ShiftAssignment
        fields = ["id", "user", "shift"]

class ShiftAssignmentDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    shift = ShiftSerializer()

    class Meta:
        model = ShiftAssignment
        fields = ["id", "user", "shift"]