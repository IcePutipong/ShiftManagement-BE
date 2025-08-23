from rest_framework.permissions import BasePermission

class IsHeadNurse(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and 
                    getattr(getattr(request.user, "profile", None), "role", None) == "head_nurse")
