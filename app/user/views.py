"""
Views for the user API.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group, Permission
from core.models import Bank, User

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    GroupSerializer,
    PermissionSerializer,
    GroupModifySerializer,
    BankSerializer,
    MeSerializer,
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
    serializer_class = MeSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class GroupViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class=GroupModifySerializer
    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return GroupSerializer
    #     else:
    #         return GroupModifySerializer

class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Permission.objects.filter(
        content_type__app_label='custom_job_manager'
    ).all()
    serializer_class = PermissionSerializer
    

class BankViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = get_user_model().objects.all()

        # Add your conditions to the queryset
        name = self.request.query_params.get('name')
        group = self.request.query_params.get('group')
        status = self.request.query_params.get('status')
        full_name = self.request.query_params.get('full_name')
        try:
            if name:
                queryset = queryset.filter(name=name)
            if full_name:
                queryset = queryset.filter(full_name=full_name)
            if status:
                queryset = queryset.filter(status=status)
            if group and int(group) > 0:
                queryset = queryset.filter(groups__id=group)
        except Exception:
            return queryset
            # raise e
        return queryset

