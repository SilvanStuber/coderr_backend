from rest_framework import permissions
from profile_app.models import Profile

class IsReviewerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.reviewer == str(request.user.pk) or request.user.is_staff

class IsCustomerProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and is_customer_profile(request)
    
def is_customer_profile(request):
    profile = Profile.objects.get(user = request.user.pk)
    if profile.type == "customer":
        return True
    else:
        return False
