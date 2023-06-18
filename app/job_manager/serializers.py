from rest_framework import serializers
from datetime import datetime
from pathlib import Path
import shutil
import logging
from django.db import transaction

from .models import (
    JobManager,
    Job,
    JobHistory,
)

from rest_framework_tus import api


logger = logging.getLogger(__name__)


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
            'src_path',
            'source',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        # try:
        with transaction.atomic():
            record_exists = Job.objects.filter(folder_path=validated_data['folder_path']).exists()
            if record_exists:
                raise serializers.ValidationError({
                    'folder_path': f"Đã tồn tại Job với đường dẫn: {validated_data['folder_path']}",
                })

            validated_data['status'] = 'new'
            today = datetime.today()
            des_folder_path = f'/Working/{today.year}/{today.month}/{today.day}'
            validated_data['des_path'] = des_folder_path

            job = super().create(validated_data)
            request = self.context.get('request', None)
            cur_user = None
            if request:
                cur_user = request.user
            JobHistory.objects.create(job=job, status='new', creator=cur_user)

            job_names = validated_data['name'].split(', ')
            for job_name in job_names:
                path_check = Path(f'{des_folder_path}/{job_name}')
                if (not path_check.exists()):
                    path_check.mkdir(parents=True)

            src_files = []
            if validated_data['source'] == 'manual':
                fileObjs = api.get_tus_upload_by_guids(validated_data['files'])
                src_files = [{
                    'path': fileObj.temporary_file_path,
                    'name': fileObj.filename
                } for fileObj in fileObjs]
            else:
                src_files = [{
                    'path': file,
                    'name': file.split('/')[-1]
                } for file in validated_data['files']]

            print('---------')
            print(src_files)
            for src_file in src_files:
                src_path = Path(src_file['path'])
                for job_name in job_names:
                    des_path = Path(f"{des_folder_path}/{job_name}/{src_file['name']}")
                    shutil.copy(src_path, des_path)

            return job
        # except Exception as e:
        #     logger.error(f"Error create job {str(e)}")
