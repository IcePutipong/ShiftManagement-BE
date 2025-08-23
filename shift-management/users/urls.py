from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ProfileDataView, RegisterUserView, LoginUserView,LogoutUserView

urlpatterns = [
    path("register", RegisterUserView.as_view()),
    path("login", LoginUserView.as_view()),
    path("refresh", TokenRefreshView.as_view()),
    path("user_profile", ProfileDataView.as_view()),
    path("logout", LogoutUserView.as_view()),
]