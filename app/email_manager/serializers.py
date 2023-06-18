from rest_framework import serializers
from email_manager import models

class EmailUserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmailUserSetting
        fields = [
            'domain',
            'max_email',
        ]


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = [
            'id',
            'primary_email',
            'password',
            'first_name',
            'last_name',
            'phone_number',
            'status',
            'cancel_date',
        ]
        read_only_fields=['id']
