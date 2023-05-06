from rest_framework import serializers
from customermanager.models import CustomerManager

class CustomerManagerSeliazer(serializers.ModelSerializer):
    class Meta:
        model = CustomerManager
        fields = ['customer_code', 'customer_name','customer_email','customer_expose','customer_style','customer_description','customer_namepay']