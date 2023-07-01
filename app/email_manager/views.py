from rest_framework import viewsets
from rest_framework.response import Response
from email_manager.models import Email, EmailUserSetting, STATUSES
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


    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        additional_data = {
            'statuses': STATUSES,
        }
        response.data['additional_data'] = additional_data

        return response

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    def destroy(self, request, *args, **kwargs):
        email = self.get_object()
        email.status = 'CANCELING'
        email.cancel_date = datetime.now()
        email.save()
        return Response(data='delete success')