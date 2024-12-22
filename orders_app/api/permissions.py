from profile_app.models import Profile
from rest_framework import permissions
    
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.business_user or request.user.is_staff:
            return True     
        return False
class IsCustomerProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and is_customer_profile(request)
    
def is_customer_profile(request):
    profile = Profile.objects.get(user = request.user.pk)
    if profile.type == "customer":
        return True
    else:
        return False