from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user


# Custom permission for users with "is_active" = True.
class IsEmployer(permissions.BasePermission):
    """
    Allows access only to "is_active" users.
    """
    def has_permission(self, request, view):
     
        employer=request.user.employer
       
        return  employer

