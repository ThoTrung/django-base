from rest_framework import viewsets
from rest_framework.response import Response
from email_manager.models import Email, EmailUserSetting
from email_manager.serializers import EmailSerializer, EmailUserSettingSerializer
from datetime import datetime


# Create your views here.

class EmailUserSettingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmailUserSetting.objects.all()
    serializer_class = EmailUserSettingSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

# override 
    def get_queryset(self):
        email  = self.request.GET.get('email', '')

        queryset = Email.objects.all()
        if email != '':
            queryset = queryset.filter(primary_email__icontains=email)
        return queryset
    
    def delete():
        pass
    
    def destroy(self, request, *args, **kwargs):
        email = self.get_object()
        email.status = 'CANCELING'
        email.cancel_date = datetime.now()
        email.save()
        return Response(data='delete success')