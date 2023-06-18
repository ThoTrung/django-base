from django.db import models
from django.contrib.postgres.fields import ArrayField
from customer_manager.models import CustomerManager
from core.models import User

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    class Meta:
        abstract = True


class UserSettingJob(BaseModel):
    key=models.CharField(max_length=50, unique=True)
    value=models.JSONField()

    def __str__(self):
        return self.key


class JobStatus(BaseModel):
    key=models.CharField(max_length=50, unique=True)
    value=models.CharField(max_length=250)

    def __str__(self):
        return self.key


class JobManager(BaseModel):
    path = models.CharField(max_length=520, db_index=True)
    checked_time = models.DateTimeField()
    status = models.ForeignKey(JobStatus, on_delete=models.CASCADE)
    files = ArrayField(models.CharField(max_length=520), blank=True, default=list)
    
    def __str__(self):
        return str(self.id) + ': ' +self.path 


JOB_STATUS = {
    'creating': {
        'text': 'Đang tạo Job',
    },
    'new': {
        'text': 'Mới',
    },
    'doing': {
        'text': 'Đang làm',
    },
    'waiting_check': {
        'text': 'Chờ check',
    },
    'checking': {
        'text': 'Đang check',
    },
    'qc_ok': {
        'text': 'QC OK',
    },
    'waiting_edit': {
        'text': 'Chờ sửa',
    },
    'qc_edit': {
        'text': 'QC sửa',
    },
    'qc_editing': {
        'text': 'QC đang sửa',
    },
    'done': {
        'text': 'Sửa xong',
    },
    'approve': {
        'text': 'Hoàn thành',
    },
}

STATUS_CHOICES = [[key, JOB_STATUS[key]['text']] for key in JOB_STATUS]

class Job(BaseModel):

    SOURCE_CHOICES = (
        ('auto', 'Tạo job tự động'),
        ('manual', 'Tạo job bằng tay'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='created_jobs')
    folder_path = models.CharField(max_length=520, db_index=True)
    name = models.CharField(max_length=520, db_index=True)
    customer = models.ForeignKey(CustomerManager, on_delete=models.CASCADE)
    files = ArrayField(models.CharField(max_length=520), blank=True, default=list)
    expose = models.CharField(max_length=255, blank=False)
    style = models.TextField(blank=False)
    note = models.TextField(blank=True, null=True)
    deadline = models.TimeField(blank=True, null=True)
    number_sub_job = models.IntegerField(blank=True, null=True)
    editor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='assignee_jobs')
    customer_price = models.FloatField(blank=True, null=True)
    editor_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES)
    des_path = models.CharField(max_length=255, blank=False, default='')
    src_path = models.CharField(max_length=255, blank=True, null=True)


class JobHistory(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_histories', blank=True, null=True)
    editor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='assignee_job_histories')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=None)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='creator_job_histories')
