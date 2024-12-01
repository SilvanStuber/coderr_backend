from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import  RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class RegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request): 
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
        else:
            data=serializer.errors      
        return Response(data)