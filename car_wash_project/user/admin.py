from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class EmployeeAdmin(UserAdmin):
    fieldsets = (
        ('Giorgi field', {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'salary', 'birthdate')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        ('NoneGiorgi', {
            'classes': ('wide',),
            'fields': (
            'email', 'password1', 'password2', 'birthdate', 'image', 'salary', 'phone_number', 'hire_date', 'status'),
        }),
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')  # ეს არ ჩანს სადაა? ვნახე, ჯგუფი არ უჩანს მხოლოდ
    search_fields = ('first_name', 'last_name', 'email')
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'status')
    ordering = ['status']
