from rest_framework.permissions import BasePermission
class CheckUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.id == obj.id)
class IsAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request)
        return bool(request.user.is_superuser or request.method == 'GET')