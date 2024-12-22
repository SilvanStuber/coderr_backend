from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.user or request.user.is_staff:
            return True     
        return False

