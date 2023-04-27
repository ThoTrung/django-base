from django.contrib import admin
from . import models

# Register your models here.
class DmDoituongAdmin(admin.ModelAdmin):
    list_display = ["madoituong", "tendoituong", "dienthoai"]
    pass
admin.site.register(models.DmDoituong,DmDoituongAdmin)


class DmNhomdoituongAdmin(admin.ModelAdmin):
    list_display = ["tennhom"]
    pass
admin.site.register(models.DmNhomdoituong,DmNhomdoituongAdmin)
