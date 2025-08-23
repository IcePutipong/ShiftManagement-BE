from django.urls import path
from .views import ShiftCreateView, ShiftAssignmentCreateView, UserScheduleView

urlpatterns = [
    path("shifts", ShiftCreateView.as_view()),
    path("shift-assignments", ShiftAssignmentCreateView.as_view()),
    path("user-schedule", UserScheduleView.as_view()),
]