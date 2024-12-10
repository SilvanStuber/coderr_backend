from rest_framework.views import APIView
from rest_framework.response import Response
from profile_app.models import Profile
from .serializers import ProfileSerializer, BusinessProfileSerializer, CustomerProfileSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class ProfileViewSets(generics.ListCreateAPIView):  
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            profiles = Profile.objects.get(user=pk)
            serializer = ProfileSerializer(profiles)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "message": "Profil nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        try:
            profile = Profile.objects.get(user=pk)
            if not (request.user == user or request.user.is_staff):
                raise PermissionDenied("Keine Berechtigung, dieses Profil zu bearbeiten.")
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "message": "Profil nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied:
            return Response({
                "message": "Keine Berechtigung, dieses Profil zu bearbeiten."
            }, status=status.HTTP_403_FORBIDDEN)
        except ValidationError as e:
            return Response({
                "errors": e.detail
            }, status=status.HTTP_400_BAD_REQUEST)

    
class ProfileCustomerViewSets(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            customer_profiles = Profile.objects.filter(type="customer")
            serializer = CustomerProfileSerializer(customer_profiles, many=True)
            print("serializer.data", serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "message": "Profil nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)
        
class ProfileBusinessViewSets(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        try:
            business_profiles = Profile.objects.filter(type="business")
            serializer = BusinessProfileSerializer(business_profiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "message": "Profil nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)
       
        