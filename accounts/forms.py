from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
# from django import forms
# from django.contrib.auth import password_validation
# from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('name', 'image',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
