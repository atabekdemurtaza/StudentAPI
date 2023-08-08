from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter


router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns = router.urls
