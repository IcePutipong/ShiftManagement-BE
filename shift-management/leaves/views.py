from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import LeaveRequest
from .serializer import LeaveReqSerializer
from users.permissions import IsHeadNurse

# Create your views here.
class LeaveReqCreateView(generics.CreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveReqSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(status=("pending"))
    
class LeaveReqListView(generics.ListAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveReqSerializer
    permission_classes = [permissions.IsAuthenticated, IsHeadNurse]

class LeaveReqApproveView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsHeadNurse]

    def patch(self, request, pk):
        try:
            leave = LeaveRequest.objects.get(pk=pk)
        except LeaveRequest.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get("status")
        if new_status not in ["approved", "rejected"]:
            return Response({"error": "Invalid Status"}, status=status.HTTP_400_BAD_REQUEST)
        
        leave.status = new_status
        leave.approved_by = request.user
        leave.save()
        return Response(LeaveReqSerializer(leave).data)

