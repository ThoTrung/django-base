"""
URL mappings for the user API.
"""
from django.urls import (
    path,
    include
)

from user import views
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, PermissionViewSet, BankViewSet, UserViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'banks', BankViewSet)
router.register(r'cusers', UserViewSet)

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('', include(router.urls)),
]
