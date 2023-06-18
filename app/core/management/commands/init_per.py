from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, ContentType

from core.models import User
from job_manager.models import JobStatus, UserSettingJob

class Command(BaseCommand):
    """Init some data"""
    def handle(self, *args, **options):
        permission_names = (
            {
                'code': 'user_manager',
                'name': 'Quản lý user',
            },{
                'code': 'role_manager',
                'name': 'Quản lý role',
            },{
                'code': 'customer_manager',
                'name': 'Quản lý khách hàng',
            },{
                'code': 'cloud_info',
                'name': 'Thông tin cloud',
            },{
                'code': 'create_job',
                'name': 'Tạo Job',
            },{
                'code': 'job_list',
                'name': 'Danh sách Job',
            },{
                'code': 'statistic',
                'name': 'Thống kê',
            },{
                'code': 'salary_calc',
                'name': 'Tính lương',
            },{
                'code': 'export_invoice',
                'name': 'Xuất hóa đơn',
            },{
                'code': 'email_manager',
                'name': 'Quản lý email',
            }
        )

        # Delete Rollback
        content_type = ContentType.objects.filter(
            app_label='custom_job_manager',
            model='custom_job_manager_model'
        ).first()
        if content_type:
            per = Permission.objects.filter(content_type_id=content_type.id)
            per.delete()
            content_type.delete()

        # Create
        content_type = ContentType.objects.create(
            app_label='custom_job_manager',
            model='custom_job_manager_model'
        )

        for p in permission_names:
            Permission.objects.create(
                codename=p['code'],
                name=p['name'],
                content_type=content_type,
            )
