from django.shortcuts import render
from django.urls import path
from customermanager.models import CustomerManager
from customermanager.serializers import CustomerManagerSeliazer
from rest_framework import viewsets


# Create your views here.

class CustomerManagerViewSet(viewsets.ModelViewSet):
    queryset = CustomerManager.objects.all()
    serializer_class = CustomerManagerSeliazer

# override 
    def get_queryset(self):
        customerName = self.request.GET.get('customer_name',None)
        customerEmail  = self.request.GET.get('customer_email',None)
        queryset = CustomerManager.objects.all();
        """
        if customerName is not None:
            if customerEmail is not None:
                return CustomerManager.objects.filter(customerName=customerName,customerEmail = customerEmail)
            else :
                return CustomerManager.objects.filter(customerName=customerName)
        elif customerEmail is not None:
            return CustomerManager.objects.filter(customerEmail = customerEmail)                                              
        """
        if customerName is not None:
            queryset = queryset.filter(customer_name=customerName)
        if customerEmail is not None:
            queryset = queryset.filter(customer_email=customerEmail)
        return queryset