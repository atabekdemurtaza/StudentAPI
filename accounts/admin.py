from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'name', 'is_staff', 'image']
    add_form = CustomUserChangeForm
    form = CustomUserCreationForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ("name", "image",)
        }),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'fields': ("name", "image",)
            }
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
