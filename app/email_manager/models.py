from django.db import models
from core import models as coreModels

# Create your models here.

class EmailUserSetting(coreModels.BaseModel):
    owner = models.OneToOneField(coreModels.User, on_delete=models.CASCADE, primary_key=True)
    domain = models.CharField(max_length=255, unique=True)
    max_email = models.PositiveIntegerField()

    def __str__(self):
        return self.domain

    

class Email(coreModels.BaseModel):
    
    STATUS_CHOICES = (
        ('NEW', 'Tài khoản mới'),
        ('WORKING', 'Tài khoản đang dùng'),
        ('CANCELED', 'Tài khoản đã bị xóa'),
    )

    primary_email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='WORKING')
    cancel_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.primary_email
