from django.contrib import admin
from . import models

# Register your models here.
class DmDoituongAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.DmDoituong,DmDoituongAdmin)


class DmNhomdoituongAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.DmNhomdoituong,DmNhomdoituongAdmin)
