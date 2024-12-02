from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from profile_app.models import Profile

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request): 
        print(request.data)
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email,
                "user_id": saved_account.pk
            }
            
            # Hier die Korrektur: Zugriff auf type
            profile_type = request.data.get('type', 'customer')  # Default auf 'customer', falls 'type' fehlt
            
            # Profil erstellen
            Profile.objects.create(
                user=saved_account,
                email=saved_account.email,
                type=profile_type, 
            )
        else:
            data = serializer.errors      
        return Response(data)
