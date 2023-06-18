from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from email_manager import views

router = DefaultRouter()
router.register('',views.EmailViewSet)
router.register('setting',views.EmailUserSettingViewSet)

urlpatterns = [
    path('',include(router.urls))
]
