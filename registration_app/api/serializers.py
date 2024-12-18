from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        if pw != repeated_pw:
            raise serializers.ValidationError({"password": ["Das Passwort ist nicht gleich mit dem wiederholten Passwort"]})       
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({"email": ["Diese E-Mail-Adresse wird bereits verwendet."]})
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({"username": ["Dieser Benutzername ist bereits vergeben."],})
        else:
          account = User(email=self.validated_data['email'], username=self.validated_data['username'])
          account.set_password(pw)
          account.save()
          return account