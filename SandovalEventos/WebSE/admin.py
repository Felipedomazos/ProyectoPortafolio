from django.contrib import admin
from .models import Cliente, Pedido, DetallePedido, Producto, Evento, Cotizacion, Contacto

# Register your models here.



admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Producto)
admin.site.register(Evento)
admin.site.register(Cotizacion)

admin.site.register(Contacto)