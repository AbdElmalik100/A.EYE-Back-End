from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class ManagingUsers(UserAdmin):
    list_display = ['__str__', 'id' ,'email', 'is_superuser']
    ordering = ('id',)

    add_fieldsets = (
            ('Main Information', {
                'classes':('wide',),
                'fields': ('first_name', 'last_name', 'username' ,'email', 'password1', 'password2'),
                }),
            ("Dates", {
                'fields': ('date_joined', 'last_login'),
            }),
            ('Permissions', {
                'fields': ('groups','user_permissions','is_staff', 'is_active', 'is_superuser')
            }),
            ('Avatar', {
                'fields': ('avatar',)
            }),
        )
    fieldsets = (
            ('Main Information', {
                'classes':('wide',),
                'fields': ('first_name', 'last_name', 'username' ,'email', 'password'),
                }),
            ("Dates", {
                'fields': ('date_joined', 'last_login'),
            }),
            ('Permissions', {
                'fields': ('groups','user_permissions','is_staff', 'is_active', 'is_superuser')
            }),
            ('Avatar', {
                'fields': ('avatar',)
            }),
        )
        


admin.site.register(CustomUser, ManagingUsers)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)