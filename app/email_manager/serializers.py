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
        read_only_fields=['id', 'status']
    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        emailUserSetting = models.EmailUserSetting.objects.filter(owner=user).first()
        if attrs['primary_email'].endswith(f"@{emailUserSetting.domain}") == False:
            raise serializers.ValidationError({"primary_email": ["không đúng định dạng",]})
        return attrs
        # return super().validate(attrs)
        
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        del validated_data['primary_email']
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class APIMailSerializer(serializers.Serializer):
    primaryEmail = serializers.CharField(required=True, max_length=256, )#example='tien.lq@htvietnam.com.vn')
    password = serializers.CharField(required=True, max_length=100, )#example='your default pass')
    familyName = serializers.CharField(required=True, max_length=100, )#example='you lastName')
    givenName = serializers.CharField(required=True, max_length=100, )#example='your fisrtName')
