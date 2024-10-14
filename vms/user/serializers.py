import pdb

from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomJWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }

        user_obj = User.objects.filter(email=attrs.get("username")).first() or User.objects.filter(
            username=attrs.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username
        data = super().validate(credentials)
        data['first_name'] = user_obj.first_name
        data['last_name'] = user_obj.last_name

        return data
