from rest_framework import serializers

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
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        validated_data['status'] = 'creating'
        validated_data['source'] = 'manual'
        job = super().create(validated_data)
        return job
