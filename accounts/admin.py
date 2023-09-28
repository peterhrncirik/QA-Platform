from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    #TODO: List All Schools/Courses User is part of

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Status', {
            'fields': ('is_instructor', 'is_student')
        }),
    )
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)