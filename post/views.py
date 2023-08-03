from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from django.views.generic import TemplateView


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser, ]


class Dashboard(TemplateView):
    template_name = 'home.html'
