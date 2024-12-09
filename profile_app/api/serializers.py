from rest_framework import serializers
from profile_app.models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'pk', 'username', 'email'] 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [    
            'user',       
            'username', 
            'first_name',
            'last_name',
            'file',
            'location',
            'tel',
            'description',
            'working_hours',
            'type',
            'email',
            'created_at',
        ]

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'file',
            'uploaded_at',
            'type',
        ]


class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'file',
            'uploaded_at', 
            "location",
            "tel",
            "description",
            "working_hours",
            'type',
        ]
        
