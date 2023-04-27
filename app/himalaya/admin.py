from django.contrib import admin
from . import models

# Register your models here.
class DmDoituongAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.DmDoituong,DmDoituongAdmin, using='himalaya')

# othersite = admin.AdminSite("himalaya")
# othersite.register(models.DmDoituong)