from django.db import models
from django.contrib.auth import get_user_model
from shifts.models import ShiftAssignment  

User = get_user_model()

# Create your models here.

class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    shift_assignment = models.ForeignKey(
        ShiftAssignment, on_delete=models.CASCADE, related_name="leave_requests"
    )
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    approved_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="approved_leaves"
    )
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      

    def __str__(self):
        return f"LeaveRequest({self.shift_assignment.user.username} - {self.shift_assignment.shift.date}) [{self.status}]"