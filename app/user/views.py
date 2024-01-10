"""
Views for the user API.
"""
from rest_framework import generics
from token.views import ObtainAuthToken

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Createe a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES