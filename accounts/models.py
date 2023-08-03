from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        upload_to='accounts/%Y/%m/%d/',
        blank=True,
        null=True)
