from rest_framework import serializers
from .models import LeaveRequest

class LeaveReqSerializer(serializers.ModelSerializer):
    class Meta: 
        model = LeaveRequest
        fields = ["id", "shift_assignment", "reason", "status", "approved_by", "created_at"]
        read_only_fields = ["status", "approved_by", "created_at"]