from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from rest_framework import routers
from solicitud.views import SolicitudViewSet

router = routers.DefaultRouter()
router.register(r'solicitudes', SolicitudViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
