from rest_framework.views import APIView
from rest_framework.response import Response
from profile_app.models import Profile
from .serializers import ProfileSerializer, BusinessProfileSerializer, CustomerProfileSerializer
from rest_framework import  mixins, generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound, ValidationError
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class ProfileViewSets(generics.ListCreateAPIView):  
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
 
   
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        print(pk)
        profiles = Profile.objects.filter(user_id=pk)
        if not profiles.exists():
            raise NotFound(detail={
                "ok": False,
                "status": 404,
                "message": "Profil nicht gefunden"
            })
        return profiles

    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            profile = self.get_object(pk)
            if not (request.user == profile.user or request.user.is_staff):
                raise PermissionDenied("Keine Berechtigung, dieses Profil zu bearbeiten.")
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "ok": True,
                "status": 200,
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "ok": False,
                "status": 404,
                "message": "Profil nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied:
            return Response({
                "ok": False,
                "status": 403,
                "message": "Keine Berechtigung, dieses Profil zu bearbeiten."
            }, status=status.HTTP_403_FORBIDDEN)
        except ValidationError as e:
            return Response({
                "ok": False,
                "status": 400,
                "errors": e.detail
            }, status=status.HTTP_400_BAD_REQUEST)

    
class ProfileCustomerViewSets(APIView):
    def get(self, request, *args, **kwargs):
        customer_profiles = Profile.objects.filter(type="customer")
        serializer = CustomerProfileSerializer(customer_profiles, many=True)
        return Response(serializer.data)

class ProfileBusinessViewSets(APIView):
       def get(self, request, *args, **kwargs):
        business_profiles = Profile.objects.filter(type="business")
        serializer = BusinessProfileSerializer(business_profiles, many=True)
        return Response(serializer.data)