from datetime import datetime, timezone, time
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

DATETIME_FORMAT = '%Y-%m-%d %H:%M'

class JobManagerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.JobManagerSerializer
    queryset = JobManager.objects.all()

    def create(self, request, *args, **kwargs):
        return Response({'error': 'Creating objects is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    # permission_classes = [IsAuthenticated]
class ListFolderFromDiskView(APIView):
    permission_classes = [IsAuthenticated]

    def _getListFileFromFolder(self, folderPath, startTime, endTime, ignoreFolders):
        folderPathObj = pathlib.Path(folderPath)
        res = {}
        for file in folderPathObj.rglob("*.*"):
            intersectionFolders = ignoreFolders.intersection(file.parents[0].parts)
            if len(intersectionFolders) == 0:
                lastModifiedTimeOfFile = datetime.fromtimestamp(file.lstat().st_mtime).strftime('%Y-%m-%d %H:%M')
                if (not startTime or lastModifiedTimeOfFile >= startTime) \
                    and (not endTime or lastModifiedTimeOfFile <= endTime):

                    folderPath = str(file.parents[0].resolve())
                    if folderPath not in res:
                        res[folderPath] = {
                            'files': [],
                            'lastModifiedFolder': '',
                            'path': pathlib.Path(folderPath).as_posix().replace(
                                '/LocalDrive', 'E:\\MyDrive'
                            ).replace(
                                '/LocalDropbox', 'E:\\Dropbox'
                            ).replace('/', '\\')
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

        ignoreFolderSetting = UserSettingJob.objects.filter(key='ignore_folder').get()
        ignoreFolders = set(ignoreFolderSetting.value['folders'])

        # searchFolderSetting = UserSettingJob.objects.filter(key='search_folder').get()
        # driverFolderPath = DRIVER_FOLDER + searchFolderSetting.value['driver']
        # dropboxFolderPath = DROPBOX_FOLDER + searchFolderSetting.value['dropbox']
        driverFolderPath = DRIVER_FOLDER + request.query_params.get('driverPath', '')
        dropboxFolderPath = DROPBOX_FOLDER + request.query_params.get('dropboxPath', '')
        startTime = request.query_params.get('startTime', None)
        endTime = request.query_params.get('endTime', None)

        driverListFiles = self._getListFileFromFolder(driverFolderPath, startTime, endTime, ignoreFolders)
        dropboxListFiles = self._getListFileFromFolder(dropboxFolderPath, startTime, endTime, ignoreFolders)

        listFiles = driverListFiles + dropboxListFiles

        return Response({'data': listFiles})



class ListSpecifyFolderFromDiskView(APIView):
    permission_classes = [IsAuthenticated]

    def _getListFileFromFolder(self, folderPath, startTime, endTime, ignoreFolders):
        folderPathObj = pathlib.Path(folderPath)
        res = {}
        for file in folderPathObj.rglob("*.*"):
            intersectionFolders = ignoreFolders.intersection(file.parents[0].parts)
            if len(intersectionFolders) == 0:
                lastModifiedTimeOfFile = datetime.fromtimestamp(file.lstat().st_mtime).strftime('%Y-%m-%d %H:%M')
                if lastModifiedTimeOfFile >= startTime and lastModifiedTimeOfFile <= endTime:
                    folderPath = str(file.parents[0].resolve())
                    if folderPath not in res:
                        res[folderPath] = {
                            'files': [],
                            'lastModifiedFolder': '',
                            'path': pathlib.Path(folderPath).as_posix().replace(
                                '/LocalDrive', 'E:\\MyDrive'
                            ).replace(
                                '/LocalDropbox', 'E:\\Dropbox'
                            ).replace('/', '\\')
                        }
                    res[folderPath]['files'].append(str(file.resolve()))

                    if lastModifiedTimeOfFile > res[folderPath]['lastModifiedFolder']:
                        res[folderPath]['lastModifiedFolder'] = lastModifiedTimeOfFile

        return list(res.values())
    
    def _getListSpecialFileFromFolder(self, folderPathObj, startTime, endTime, ignoreFolders):
        res = {}
        for file in folderPathObj.rglob("*.*"):
            parent = file.parents[0]
            parentPath = str(parent.resolve())
            if parentPath not in res:
                lastModifiedTimeOfFolder = parent.lstat().st_mtime
                if lastModifiedTimeOfFolder >= startTime and lastModifiedTimeOfFolder <= endTime:
                    intersectionFolders = ignoreFolders.intersection(parent.parts)
                    if len(intersectionFolders) == 0:
                        tempRes = {
                            'files': [],
                            'count': 0,
                            'lastModifiedFolder': lastModifiedTimeOfFolder,
                            'path': pathlib.Path(parentPath).as_posix().replace(
                                '/LocalDrive', 'E:\\MyDrive'
                            ).replace(
                                '/LocalDropbox', 'E:\\Dropbox'
                            ).replace('/', '\\')
                        }
                        for file in parent.glob("*.*"):
                            # lastModifiedTimeOfFile = file.lstat().st_mtime
                            # if lastModifiedTimeOfFile >= startTime and lastModifiedTimeOfFile <= endTime and file.name not in ignoreFolders:
                            if file.name not in ignoreFolders:
                                # tempRes['files'].append(str(file.resolve()))
                                tempRes['count'] += 1
                        if tempRes['count'] > 0:
                            res[parentPath] = tempRes

        return list(res.values())


    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        DRIVER_FOLDER = '/LocalDrive/'
        DROPBOX_FOLDER = '/LocalDropbox/'
        MIN_TIMESTAMP = 0
        MAX_TIMESTAMP = 4839578483

        driverPathparam = request.query_params.get('driverPath', '')
        dropboxPathparam = request.query_params.get('dropboxPath', '')
        startTime = request.query_params.get('startTime', None)
        endTime = request.query_params.get('endTime', None)
        startTime = MIN_TIMESTAMP if startTime == '' else datetime.strptime(startTime, DATETIME_FORMAT).timestamp()
        endTime = MAX_TIMESTAMP if endTime == '' else datetime.strptime(endTime, DATETIME_FORMAT).timestamp()

        ignoreFolderSetting = UserSettingJob.objects.filter(key='ignore_folder').get()
        ignoreFolders = set(ignoreFolderSetting.value['folders'])

        driverListFiles = []
        dropboxListFiles = []
        if driverPathparam == '' or driverPathparam == '.':
            for path in pathlib.Path(DRIVER_FOLDER).glob('- 02*/Input/*/'):
                if path.is_dir(): # and (startTime is None or startTime <= latestModifiedFolderTime) and (endTime is None or endTime >= latestModifiedFolderTime):
                    driverListFiles = driverListFiles + self._getListSpecialFileFromFolder(path, startTime, endTime, ignoreFolders)
        else:
            driverPathparam = pathlib.Path(DRIVER_FOLDER + driverPathparam).as_posix().replace('\\', '/')
            driverListFiles = self._getListSpecialFileFromFolder(pathlib.Path(driverPathparam), startTime, endTime, ignoreFolders)

        if dropboxPathparam == '' or dropboxPathparam == '.':
            for path in pathlib.Path(DROPBOX_FOLDER).glob('- 01*/Input/*/'):
                if path.is_dir(): # and (startTime is None or startTime <= latestModifiedFolderTime) and (endTime is None or endTime >= latestModifiedFolderTime):
                    dropboxListFiles = dropboxListFiles + self._getListSpecialFileFromFolder(path, startTime, endTime, ignoreFolders)
        else:
            dropboxPathparam = pathlib.Path(DROPBOX_FOLDER + dropboxPathparam).as_posix().replace('\\', '/')
            dropboxListFiles = self._getListSpecialFileFromFolder(pathlib.Path(dropboxPathparam), startTime, endTime, ignoreFolders)


        listFiles = driverListFiles + dropboxListFiles

        return Response({'data': listFiles})

class SearchFolderSettingView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        searchFolder = UserSettingJob.objects.filter(key='search_folder').get()
        driverPosixPath = searchFolder.value['driver']
        dropboxPosixPath = searchFolder.value['dropbox']

        driverWindowPath = pathlib.Path(driverPosixPath).as_posix().replace('/', '\\')
        dropboxWindowPath = pathlib.Path(dropboxPosixPath).as_posix().replace('/', '\\')

        return Response({'data': {
            'driver': driverWindowPath,
            'dropbox': dropboxWindowPath
        }})


    def put(self, request):
        windowPath = request.data.get('value', '')
        subkey = request.data.get('subkey', '')

        posixPath = pathlib.Path(windowPath).as_posix().replace('\\', '/')
        searchFodlerObj = UserSettingJob.objects.filter(key='search_folder').get()
        searchFodlerObj.value[subkey] = posixPath
        searchFodlerObj.save()
        return Response({'data': 'Ok'})
