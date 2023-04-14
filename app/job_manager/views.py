from datetime import datetime, timezone
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework import (
    viewsets,
    mixins,
    status,
)
import pathlib 
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    JobManager, JobStatus, UserSettingJob
)
from . import serializers

class JobManagerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.JobManagerSerializer
    queryset = JobManager.objects.all()

    def create(self, request, *args, **kwargs):
        return Response({'error': 'Creating objects is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    # permission_classes = [IsAuthenticated]

class ListFolderFromDiskView(APIView):
    permission_classes = [IsAuthenticated]

    def _getListFileFromFolder(self, folderPath, startTime, endTime):
        folderPathObj = pathlib.Path(folderPath)
        res = {}
        for file in folderPathObj.rglob("*.*"):
            lastModifiedTimeOfFile = datetime.fromtimestamp(file.lstat().st_mtime).strftime('%Y-%m-%d %H:%M')
            if (not startTime or lastModifiedTimeOfFile >= startTime) \
                and (not endTime or lastModifiedTimeOfFile <= endTime):

                folderPath = str(file.parents[0].resolve())
                if folderPath not in res:
                    res[folderPath] = {
                        'files': [],
                        'lastModifiedFolder': '',
                        'path': folderPath
                    }
                res[folderPath]['files'].append(str(file.resolve()))

                if lastModifiedTimeOfFile > res[folderPath]['lastModifiedFolder']:
                    res[folderPath]['lastModifiedFolder'] = lastModifiedTimeOfFile

        return list(res.values())


    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        DRIVER_FOLDER = '/LocalDrive/'
        DROPBOX_FOLDER = '/LocalDropbox/'

        driverFolderPath = DRIVER_FOLDER + request.query_params.get('driverPath', '')
        dropboxFolderPath = DROPBOX_FOLDER + request.query_params.get('dropboxPath', '')
        startTime = request.query_params.get('startTime', None)
        endTime = request.query_params.get('endTime', None)

        driverListFiles = self._getListFileFromFolder(driverFolderPath, startTime, endTime)
        dropboxListFiles = self._getListFileFromFolder(dropboxFolderPath, startTime, endTime)

        listFiles = driverListFiles + dropboxListFiles

        return Response({'data': listFiles})


class UserSettingJobViewGet(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        folderSettings = UserSettingJob.objects.filter(key__in=('driver', 'dropbox')).values('key', 'value')
        folderSettingsIndict = {d['key']: d['value'] for d in folderSettings}
        return Response({'data': folderSettingsIndict})


class UserSettingJobViewPut(APIView):
    # permission_classes = [IsAuthenticated]
    def put(self, request, key):
        value = request.query_params.get('value', '')
        UserSettingJob.objects.filter(key=key).update(value=value)
        print(key)
        return Response({'data': 'Ok'})