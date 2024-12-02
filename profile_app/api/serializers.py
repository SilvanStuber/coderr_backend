from rest_framework import serializers
from profile_app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField() 

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

class BusinessProfileSerializer(serializers.ModelSerializer):
    user = ProfileSerializer 

    class Meta:
        model = Profile
        fields = [
            'user',
            'file',
            'location',
            'tel',
            'description',
            'working_hours',
            'type'
        ]

class CustomerProfileSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()  # Geschachtelte User-Daten

    class Meta:
        model = Profile
        fields = [
            'user',
            'file',
            'uploaded_at',
            'type'
        ]
