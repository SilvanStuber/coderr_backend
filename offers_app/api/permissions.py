from rest_framework import permissions
from profile_app.models import Profile

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.user or request.user.is_staff:
            return True     
        return False

class IsBusinessProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and is_business_profile(request)
    
def is_business_profile(request):
    profile = Profile.objects.get(user = request.user.pk)
    if profile.type == "business":
        return True
    else:
        return False