from django.urls import URLPattern, path
from WebSE import views
from .views import Inicio, Nosotros,  Matrimonio, Celebracion, CoffeeBreak, Tabla, Desayuno, Administracion, adminTablas, adminDesayunos, Cotizaciones, Cuenta, actualizar_cliente, Registro, Login, cerrar_sesion, EliminarObjeto, EliminarCliente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('nosotros/', Nosotros, name="nosotros"),
    path('matrimonio/', Matrimonio, name="matrimonio"),
    path('celebracion/', Celebracion, name="celebracion"),
    path('coffeebreak/', CoffeeBreak, name="coffeebreak"),
    path('tabla/', Tabla, name="tabla"),
    path('desayuno/', Desayuno, name="desayuno"),
    path('administracion/', Administracion, name="administracion"),
    path('adminTablas/', adminTablas, name="adminTablas"),
    path('adminDesayunos/', adminDesayunos, name="adminDesayunos"),
    path('cotizaciones/', Cotizaciones, name="cotizaciones"),
    path('registro/', Registro, name="registro"),
    path('login/', Login, name="login"),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('cuenta/', Cuenta, name='cuenta'),
    path('actualizar-cliente/', actualizar_cliente, name='actualizar_cliente'),
    path('eliminar/<str:pk>/', EliminarObjeto.as_view(), name='adminTablas'),
    path('eliminar_cliente/<int:pk>/', EliminarCliente.as_view(), name='administracion')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)