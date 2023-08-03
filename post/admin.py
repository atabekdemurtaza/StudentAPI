from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', ]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', ]
