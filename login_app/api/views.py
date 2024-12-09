from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import CustomLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class CostomLoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        request.data['username'] = generate_username(request)
        serializer = CustomLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email,
                "user_id": user.id,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def generate_username(request):
    username = request.data.get('username', '') 
    if ' ' in username:
            username = username.replace(' ', '_')
    return username.lower()