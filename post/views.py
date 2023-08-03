from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from .models import Post
from .serializers import PostSerializer
from django.views.generic import TemplateView


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Dashboard(TemplateView):
    template_name = 'home.html'
