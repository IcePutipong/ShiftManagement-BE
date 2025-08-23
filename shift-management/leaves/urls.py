from django.urls import path
from .views import LeaveReqCreateView, LeaveReqListView, LeaveReqApproveView

urlpatterns = [
    path("leave-requests", LeaveReqCreateView.as_view()),
    path("leave-requests/all", LeaveReqListView.as_view()),
    path("leave-requests/<int:pk>/approve", LeaveReqApproveView.as_view()),
]
