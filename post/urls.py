from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path(
        '<slug:slug>/<int:pk>/',
        views.PostDetail.as_view(),
        name='post_detail'
    ),
]
