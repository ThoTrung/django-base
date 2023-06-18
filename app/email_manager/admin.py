from django.contrib import admin
from email_manager import models

# Register your models here.
admin.site.register(models.EmailUserSetting)
admin.site.register(models.Email)