from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    class Meta:
        abstract=True

        
class CustomerManager(BaseModel):
    code = models.CharField(max_length=50, unique=True, blank=False)
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    expose = models.CharField(max_length=255, blank=False)
    style = models.TextField(blank=False)
    pay_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    contact_channel=models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    deadline = models.TimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
