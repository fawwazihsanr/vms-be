from rest_framework_simplejwt.views import TokenObtainPairView

from vms.user.serializers import CustomJWTSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
