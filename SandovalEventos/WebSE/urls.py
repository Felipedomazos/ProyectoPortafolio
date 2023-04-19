from django.urls import URLPattern, path
from WebSE import views
from .views import Inicio


urlpatterns = [
    path('', Inicio, name="Inicio"),
]
