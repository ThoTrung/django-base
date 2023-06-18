from rest_framework import viewsets
from email_manager.models import Email, EmailUserSetting
from email_manager.serializers import EmailSerializer, EmailUserSettingSerializer


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
            queryset = queryset.filter(primaryEmail__icontains=email)
        return queryset