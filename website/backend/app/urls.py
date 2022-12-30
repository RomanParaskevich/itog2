from garpixcms.urls import *  # noqa
from django.urls import path, include
from django.contrib import admin
from .yasg import urlpatterns as doc_urls


urlpatterns = [path('admin/', admin.site.urls)]

urlpatterns = [path('api/v1/albums/', include('album.urls')),
               path('api/v1/register/', include('authentication.urls')),
               ] + urlpatterns  # noqa

urlpatterns += [
    path('api/v1/auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += doc_urls
