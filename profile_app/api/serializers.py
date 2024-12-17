from rest_framework import serializers
from profile_app.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile  # Das Modell muss explizit angegeben werden
        fields = ['pk', 'username', 'first_name', 'last_name']

        def get_user(self, obj):
            user_id = serializers.SerializerMethodField()
            profile = Profile.objects.get(id=user_id)
            return {
                'pk': user_id,
                'username': profile .username,
                'first_name': profile .first_name,
                'last_name': profile .last_name,
            }

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

    

    
    
        
