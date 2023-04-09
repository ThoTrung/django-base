from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    class Meta:
        abstract = True


class UserSettingJob(BaseModel):
    key=models.CharField(max_length=50, unique=True)
    value=models.CharField(max_length=520)

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

