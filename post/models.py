from django.db import models
from django.conf import settings

from django.urls import reverse


"""class Author(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        self.name

    @property
    def fullname(self):
        return f"User's fullname is {self.name}"
"""


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    slug = models.SlugField(
        verbose_name='url',
        max_length=500,
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='post/%Y/%m/%d/',
        blank=True,
        null=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'post_detail',
            args=[self.pk]
        )
