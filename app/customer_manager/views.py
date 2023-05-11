from django.shortcuts import render
from django.urls import path
from customer_manager.models import CustomerManager
from customer_manager.serializers import CustomerManagerSeliazer
from rest_framework import viewsets


# Create your views here.

class CustomerManagerViewSet(viewsets.ModelViewSet):
    queryset = CustomerManager.objects.all()
    serializer_class = CustomerManagerSeliazer

# override 
    def get_queryset(self):
        name = self.request.GET.get('name', '')
        email  = self.request.GET.get('email', '')

        queryset = CustomerManager.objects.all()
        if name != '':
            queryset = queryset.filter(name__icontains=name)
        if email != '':
            queryset = queryset.filter(email__icontains=email)
        return queryset