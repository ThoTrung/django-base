from rest_framework import serializers
from datetime import datetime
from pathlib import Path
import shutil
import logging

from .models import (
    JobManager,
    JobStatus,
    UserSettingJob,
    Job,
)

from rest_framework_tus import api


logger = logging.getLogger(__name__)

print(__name__)

class JobManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobManager
        fields = [
            'id', 'path', 'checked_time', 'status', 'files'
        ]
        read_only_fields = ['id']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id',
            'folder_path',
            'name',
            'customer',
            'files',
            'expose',
            'style',
            'note',
            'deadline',
            'number_sub_job',
            'editor',
            'customer_price',
            'editor_price',
            'des_path',
            'src_path'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        logger.warning("Create Job ......")

        validated_data['status'] = 'creating'
        validated_data['source'] = 'manual'
        today = datetime.today()
        des_folder_path = f'/Working/{today.year}/{today.month}/{today.day}'
        validated_data['des_path'] = des_folder_path
        job_names = validated_data['name'].split(', ')

        for job_name in job_names:
            path_check = Path(f'{des_folder_path}/{job_name}')
            if (not path_check.exists()):
                path_check.mkdir(parents=True)


        fileObjs = api.get_tus_upload_by_guids(validated_data['files'])
        for fileObj in fileObjs:
            src_path = Path(fileObj.temporary_file_path)
            for job_name in job_names:
                des_path = Path(f'{des_folder_path}/{job_name}/{fileObj.filename}')
                shutil.copy(src_path, des_path)

        job = super().create(validated_data)
        return job
