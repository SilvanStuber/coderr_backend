from rest_framework import permissions

class IsReviewerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.reviewer == request.user or request.user.is_staff


class IsCustomerProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_customer', False)