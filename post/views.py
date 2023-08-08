from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.views.generic import TemplateView
from rest_framework import viewsets
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

"""
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser, ]"""

"""class PostViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)"""


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class Dashboard(TemplateView):
    template_name = 'home.html'
