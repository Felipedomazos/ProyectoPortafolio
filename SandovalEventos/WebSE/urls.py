from django.urls import URLPattern, path
from WebSE import views
from .views import Inicio, Matrimonio, Celebracion, Tabla, Desayuno


urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('matrimonio/', Matrimonio, name="matrimonio"),
    path('celebracion/', Celebracion, name="celebracion"),
    path('tabla/', Tabla, name="tabla"),
    path('desayuno/', Desayuno, name="desayuno")
]
