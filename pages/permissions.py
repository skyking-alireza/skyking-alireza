from rest_framework.permissions import BasePermission , SAFE_METHODS

class RUDPagePermission(BasePermission):
    def has_permission(self, request, view):
        print(bool(request.method in SAFE_METHODS or request.user.is_superuser))
        return bool(request.method in SAFE_METHODS or request.user.is_superuser)
    
    
    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or request.user.is_superuser)