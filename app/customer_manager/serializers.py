from rest_framework import serializers
from customer_manager.models import CustomerManager

class CustomerManagerSeliazer(serializers.ModelSerializer):
    class Meta:
        model = CustomerManager
        fields = [
            'id',
            'code',
            'name',
            'email',
            'expose',
            'style',
            'pay_name',
            'phone_number',
            'contact_channel',
            'description',
        ]
        read_only_fields=['id']