from __future__ import print_function

import os.path
from drf_spectacular.utils import extend_schema, inline_serializer
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from email_manager.models import Email, EmailUserSetting, STATUSES
from email_manager.serializers import EmailSerializer, EmailUserSettingSerializer, APIMailSerializer
from datetime import datetime


SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']

# Create your views here.
class ApiMail(APIView):

    def getGoolgeService(self):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('admin', 'directory_v1', credentials=creds)
        return service
    
    def get_serializer(self, request, format=None):
        return EmailUserSettingSerializer

    def get(self, request, format=None):
        service = self.getGoolgeService()
        # Call the Admin SDK Directory API
        print('Getting the first 100 users in the domain')
        results = service.users().list(
            customer='my_customer',
            maxResults=300,
            orderBy='email'
        ).execute()
        users = results.get('users', [])
        return Response(users)
    
    @extend_schema(
        summary="Create Email",
        description="You can create email here",
        request=APIMailSerializer,
    )
    def post(self, request, *args, **kwargs):
        serializer = APIMailSerializer(data=request.data)

        try:
            if serializer.is_valid():
                service = self.getGoolgeService()
                valid_data = serializer.data
                body = {
                    'primaryEmail': valid_data['primaryEmail'],
                    'password': valid_data['password'],
                    'isMailboxSetup': True,
                    'changePasswordAtNextLogin': True,
                    'name': { # Holds the given and family names of the user, and the read-only `fullName` value. The maximum number of characters in the `givenName` and in the `familyName` values is 60. In addition, name values support unicode/UTF-8 characters, and can contain spaces, letters (a-z), numbers (0-9), dashes (-), forward slashes (/), and periods (.). For more information about character usage rules, see the [administration help center](https://support.google.com/a/answer/9193374). Maximum allowed data size for this field is 1KB.
                        'displayName': valid_data['givenName'], # The user's display name. Limit: 256 characters.
                        'familyName': valid_data['familyName'], # The user's last name. Required when creating a user account.
                        'fullName': f"{valid_data['familyName']} {valid_data['givenName']}", # The user's full name formed by concatenating the first and last name values.
                        'givenName': valid_data['givenName'], # The user's first name. Required when creating a user account.
                    },
                }
                res = service.users().insert(body=body).execute()
                return Response(res)
        except Exception as e:
            print(e.args)
            return Response(str(e))

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # def put(self, request, *args, **kwargs):
    #     pass

    # def patch(self, request, *args, **kwargs):
    #     pass

    # def delete(self, request, *args, **kwargs):
    #     pass




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