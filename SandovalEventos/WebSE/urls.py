from django.urls import URLPattern, path
from WebSE import views
from .views import Inicio, Nosotros, Matrimonio, galeria, eliminar_cotizacion, detalleCotizacion, agregar_servicio_cotizacion, Carro, detalleFacturacion, mostrarDetalle, Celebracion, CoffeeBreak, Tabla, Desayuno, Administracion, adminTablas, adminDesayunos, adminMatrimonio, Cotizaciones, Cuenta, actualizar_cliente, Registro, Login, cerrar_sesion, EliminarObjeto, EliminarCliente, EliminarServicio
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
    path('adminMatrimonio/', adminMatrimonio, name="adminMatrimonio"),
    path('cotizaciones/', Cotizaciones, name="cotizaciones"),
    path('registro/', Registro, name="registro"),
    path('login/', Login, name="login"),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('cuenta/', Cuenta, name='cuenta'),
    path('actualizar-cliente/', actualizar_cliente, name='actualizar_cliente'),
    path('eliminar/<str:pk>/', EliminarObjeto.as_view(), name='adminTablas'),
    path('eliminar/<str:pk>/', EliminarObjeto.as_view(), name='adminDesayunos'),
    path('eliminar_cliente/<int:pk>/', EliminarCliente.as_view(), name='administracion'),
    path('eliminar_servicio/<int:pk>/', EliminarServicio.as_view(), name='adminMatrimonio'),
    path('detalle/<str:producto_nombre>', mostrarDetalle, name='detalle'),
    path('agregar-al-carrito/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', Carro, name='carrito'),
    path('eliminar-del-carrito/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('detalle-facturacion/', detalleFacturacion, name='detalleFacturacion'),
    path('agregar-servicio-cotizacion/', agregar_servicio_cotizacion, name='agregar_servicio_cotizacion'),
    path('detalle-cotizacion/<str:cotizacion_nombre>', detalleCotizacion, name='detalle_cotizacion'),
    path('eliminar_cotizacion/', eliminar_cotizacion, name='eliminar_cotizacion'),
    path('eliminar-servicio-cotizacion/', views.eliminar_servicio_cotizacion, name='eliminar_servicio_cotizacion'),
    path('galeria/', galeria, name='galeria')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)