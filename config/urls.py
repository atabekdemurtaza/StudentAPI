from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from post.views import Dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/', include('post.urls')),
    path('', Dashboard.as_view(), name='dashboard'),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'api/dj-rest-auth/registration/',
        include('dj_rest_auth.registration.urls')
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
