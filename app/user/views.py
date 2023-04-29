"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group, Permission

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    GroupSerializer,
    PermissionSerializer,
    GroupModifySerializer,
)

from rest_framework import (
    viewsets,
    mixins,
    status,
)

# We can custome here to get more infor of User,
# And we can use api/me to get all current user infor after login.
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user or self.context['request'].user
        # Include additional user information in response data
        data['name'] = user.name
        data['email'] = user.email
        # Add any other user information that you want to include
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupSerializer
        else:
            return GroupModifySerializer

class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Permission.objects.filter(
        content_type__app_label='custom_job_manager'
    ).all()
    serializer_class = PermissionSerializer
    
