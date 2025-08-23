from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Shift, ShiftAssignment
from .serializers import ShiftAssignmentDetailSerializer, ShiftSerializer, ShiftAssignmentSerializer
from users.permissions import IsHeadNurse
# Create your views here.

class ShiftCreateView(generics.CreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [permissions.IsAuthenticated, IsHeadNurse]

class ShiftAssignmentCreateView(generics.CreateAPIView):
    queryset = ShiftAssignment.objects.all()
    serializer_class = ShiftAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsHeadNurse]

    def create(self, request, *args, **kwargs):
        print("DEBUG request.data:", request.data)
        return super().create(request, *args, **kwargs)

class UserScheduleView(generics.ListAPIView):
    serializer_class = ShiftAssignmentDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ShiftAssignment.objects.filter(user=self.request.user)