from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'author',
            'created_at',
            'updated_at',
            'slug'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']
