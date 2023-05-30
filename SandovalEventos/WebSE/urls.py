from django.urls import URLPattern, path
from WebSE import views
from .views import Inicio, Matrimonio, Celebracion, Tabla, Desayuno, Administracion, adminTablas, Registro

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('matrimonio/', Matrimonio, name="matrimonio"),
    path('celebracion/', Celebracion, name="celebracion"),
    path('tabla/', Tabla, name="tabla"),
    path('desayuno/', Desayuno, name="desayuno"),
    path('administracion/', Administracion, name="administracion"),
    path('adminTablas/', adminTablas, name="adminTablas"),
    path('registro/', Registro, name="registro")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)