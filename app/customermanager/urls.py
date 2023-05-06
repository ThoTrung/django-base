from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customermanager.views import CustomerManagerViewSet

router = DefaultRouter()
router.register('',CustomerManagerViewSet)

urlpatterns = [
    path('',include(router.urls))
]




# Create your views here.
