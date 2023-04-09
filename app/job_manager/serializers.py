from rest_framework import serializers

from .models import (
    JobManager,
    JobStatus,
    UserSettingJob
)

class JobManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobManager
        fields = [
            'id', 'path', 'checked_time', 'status', 'files'
        ]
        read_only_fields = ['id']