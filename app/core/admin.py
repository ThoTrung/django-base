"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission, ContentType

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['name', 'email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal Info'),
            {
                'fields': (
                    'name',
                    'full_name',
                    'gender',
                    'phone_number',
                    'address',
                    'bank',
                    'bank_number',
                    'status'
                )
            }
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


admin.site.register(models.User, UserAdmin)

class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content_type', 'codename']
    list_filter = ['content_type']
    search_fields = ['name', 'codename']
    ordering = ['content_type', 'codename']

admin.site.register(Permission, PermissionAdmin)

class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'app_label', 'model']
    list_filter = ['app_label']
    search_fields = ['app_label', 'model']
    ordering = ['app_label', 'model']

admin.site.register(ContentType, ContentTypeAdmin)

admin.site.register(models.Bank)
