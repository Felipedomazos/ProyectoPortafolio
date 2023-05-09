from django.urls import URLPattern, path
from WebSE import views
from .views import Inicio, Matrimonio


urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('matrimonio/', Matrimonio, name="matrimonio")
]
