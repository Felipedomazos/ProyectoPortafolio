from django.urls import URLPattern, path
from WebSE import views
from .views import Inicio, Matrimonio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('matrimonio/', Matrimonio, name="matrimonio")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)