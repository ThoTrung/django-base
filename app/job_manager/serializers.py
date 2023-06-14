from rest_framework import serializers
from datetime import datetime

from .models import (
    JobManager,
    JobStatus,
    UserSettingJob,
    Job,
)

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
        validated_data['status'] = 'creating'
        validated_data['source'] = 'manual'
        today = datetime.today()
        validated_data['des_path'] = f'${today.year}/${today.month}/${today.day}/'
        job = super().create(validated_data)
        return job
