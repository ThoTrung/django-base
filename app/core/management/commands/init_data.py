from django.core.management.base import BaseCommand

from core.models import User
from job_manager.models import JobStatus, UserSettingJob

class Command(BaseCommand):
    """Init some data"""
    def handle(self, *args, **options):
        # JobStatus.objects.all().delete()
        # UserSettingJob.objects.all().delete()

        JobStatus.objects.bulk_create([
            JobStatus(key='not_a_job', value='Chưa tạo job'),
            JobStatus(key='new', value='Đã tạo job'),
        ])

        UserSettingJob.objects.bulk_create([
            UserSettingJob(key='driver', value='/LocalDrive'),
            UserSettingJob(key='dropbox', value='/LocalDropbox'),
        ])