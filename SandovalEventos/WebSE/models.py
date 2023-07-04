from django.db import models
import uuid

tipos_eventos_choices = [
    ('matrimonio', 'Matrimonio'),
    ('cumpleaños', 'Cumpleaños'),
    ('aniversario', 'Aniversario'),
    ('fiesta_corporativa', 'Fiesta Corporativa'),
    ('coffee_break', 'Coffee Break'),
]

tipo_servicio_choices = [
    ('bar', 'Bar'),
    ('aperitivos', 'Aperitivos'),
    ('entrada', 'Entrada'),
    ('plato_principal', 'Plato Principal'),
    ('postre', 'Postre'),
    ('personal', 'Personal'),
    ('vajilla_cristaleria', 'Vajilla y Cristalería'),
    ('decoracion', 'Decoración'),
    ('torta', 'Torta'),
    ('catering', 'Catering'),
    ('juegos_inflables', 'Juegos Inflables'),
    ('arreglo_floral', 'Arreglo Floral'),
    ('etretenimiento', 'Entretenimiento'),
    ('transporte', 'Transporte'),
]

subtipo_servicio_choices = [
    ('destilado', 'Destilado'),
    ('bebida', 'Bebida'),
    ('bar_adicional', 'Bar Adicional'),
    ('canapes', 'Canapés'),
    ('tapaditos', 'Tapaditos'),
    ('brochetas', 'Brochetas'),
    ('empanadas_cocktail', 'Empanadas Cocktail'),
    ('menu_normal', 'Menu Normal'),
    ('menu_ninos', 'Menu Niños'),
    ('bartender', 'Bartender'),
    ('garzón/a', 'Garzón/a'),
    ('cocinero', 'Cocinero'),
    ('fotógrafo/a', 'Fotógrafo/a'),
    ('dj', 'DJ'),
    ('vajilla', 'Vajilla'),
    ('cristaleria', 'Cristaleria'),
    ('manteleria', 'Manteleria'),
    ('mesas', 'Mesas'),
    ('sillas', 'Sillas'),
    ('otros', 'Otros'),
    ('bebestible', 'Bebestible'),
    ('bocadillo_salado', 'Bocadillo Saladao'),
    ('bocadillo_dulce', 'Bocadillo Dulce'),

]


class Rol(models.Model):
    nombre = models.CharField(max_length=255)


class Cliente(models.Model):
    rutCliente = models.IntegerField(primary_key=True, verbose_name='RUT del Cliente')
    nombreCliente = models.CharField(max_length=20, verbose_name='Nombre del Cliente')
    apellidoCliente = models.CharField(max_length=20, verbose_name='Apellido del Cliente')
    correoCliente = models.EmailField(max_length=40, verbose_name='Correo del Cliente')
    fonoCliente = models.IntegerField(verbose_name='Fono del Cliente')
    direccionCliente = models.CharField(max_length=50, verbose_name='Direccion del Cliente')
    contraseñaCliente = models.CharField(max_length=50, default='')
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["nombreCliente", "apellidoCliente"]

    def __str__(self):
        return self.nombreCliente


class Tarjeta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='tarjetas')
    nombreTitular = models.CharField(max_length=50, verbose_name='Nombre del Titular')
    numeroTarjeta = models.CharField(max_length=16, verbose_name='Número de la Tarjeta')
    fechaExpiracion = models.CharField(max_length=7, verbose_name='Fecha de Expiración (MM/YY)')
    codigoSeguridad = models.CharField(max_length=4, verbose_name='Código de Seguridad')
    rutTitular = models.IntegerField(verbose_name='RUT del Titular')

    def __str__(self):
        return self.nombreTitular


class Pedido(models.Model):
    idPedido = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='ID del Pedido')
    fechaPedido = models.DateField(blank=True, verbose_name='Fecha del Pedido')
    fechaEntrega = models.DateField(blank=True, verbose_name='Fecha Entrega del Pedido')
    precioPedido = models.IntegerField(verbose_name='Precio del Pedido')

    class Meta:
        ordering = ["-fechaEntrega"]

    def __str__(self):
        return self.idPedido


class DetallePedido(models.Model):
    cantProducto = models.IntegerField(verbose_name='Cantidad del o los Productos')
    idPedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, related_name='detalles_pedido')
    idProducto = models.ForeignKey(Pedido, on_delete=models.PROTECT,verbose_name='ID del Producto')
    rutCliente = models.ForeignKey(Cliente, on_delete=models.PROTECT,max_length=9, verbose_name='RUT del Cliente')

    def __str__(self):
        return self.idPedido


class Producto(models.Model):
    idProducto = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='ID del Producto')
    nombreProducto = models.CharField(max_length=30,verbose_name='Nombre del Producto')
    descProducto = models.CharField(max_length=200,verbose_name='Descripcion del Producto')
    cantPersonas = models.IntegerField(verbose_name='Cantidad de Personas Maximas para el producto', default='0')
    precioProducto = models.IntegerField(verbose_name='Precio del Producto')
    imagenProducto = models.ImageField(upload_to='img/', default='0')

    def __str__(self):
        return self.nombreProducto

    def to_dict(self):
        return {
            'nombreProducto': self.nombreProducto,
            'cantPersonas': self.cantPersonas,
            'precioProducto': self.precioProducto,
        }


class Servicio(models.Model):
    nombreServicio = models.CharField(max_length=100, verbose_name='Nombre del Servicio')
    descServicio = models.CharField(max_length=200,verbose_name='Descripción del Servicio', default='', blank=True)
    nombrePersona = models.CharField(max_length=100, verbose_name='Nombre de quien imparte el servicio', default='', blank=True)
    precioServicio = models.IntegerField(verbose_name='Precio del Servicio')
    tipo_evento = models.CharField(
        max_length=20, choices=tipos_eventos_choices, default='matrimonio'
    )
    tipo_servicio = models.CharField(
        max_length=30, choices=tipo_servicio_choices, default='bar'
    )
    subtipo_servicio = models.CharField(
        max_length=100, choices=subtipo_servicio_choices, default='', blank=True
    )
    imagenServicio = models.ImageField(upload_to='img/', default='none', blank=True)

    def __str__(self):
        return self.nombreServicio

    def save(self, *args, **kwargs):
        if self.tipo_evento == 'matrimonio':
            if self.tipo_servicio == 'bar': 
                self.subtipo_servicio_choices = [
                    ('destilado', 'Destilado'),
                    ('bebida', 'Bebida'),
                    ('bar_adicional', 'Bar Adicional'),
                ]
            elif self.tipo_servicio == 'aperitivos':
                self.subtipo_servicio_choices = [
                    ('canapes', 'Canapés'),
                    ('tapaditos', 'Tapaditos'),
                    ('brochetas', 'Brochetas'),
                    ('empanadas_cocktail', 'Empanadas Cocktail'),
                ]
            elif self.tipo_servicio == 'entrada':
                self.subtipo_servicio_choices = [
                    ('menu_normal', 'Menu Normal'),
                    ('menu_ninos', 'Menu Niños'),
                ]
            elif self.tipo_servicio == 'personal':
                self.subtipo_servicio_choices = [
                    ('bartender', 'Bartender'),
                    ('garzón/a', 'Garzón/a'),
                    ('fotógrafo/a', 'Fotógrafo/a'),
                    ('cocinero', 'Cocinero'),
                    ('dj', 'DJ')
                ]
            elif self.tipo_servicio == 'vajilla_cristaleria':
                self.subtipo_servicio_choices = [
                    ('vajilla', 'Vajilla'),
                    ('cristaleria', 'Cristaleria')
                ]
            elif self.tipo_servicio == 'decoracion':
                self.subtipo_servicio_choices = [
                    ('manteleria', 'Manteleria'),
                    ('mesas', 'Mesas'),
                    ('sillas', 'Sillas'),
                    ('otros', 'Otros')
                ]
        elif self.tipo_evento == 'cumpleaños':
            if self.tipo_servicio == 'bar':
                self.subtipo_servicio_choices = [
                    ('tragos', 'Tragos'),
                    ('bar_adicional', 'Bar Adicional'),
                ]
            elif self.tipo_servicio == 'aperitivos':
                self.subtipo_servicio_choices = [
                    ('canapes', 'Canapés'),
                    ('tapaditos', 'Tapaditos'),
                    ('brochetas', 'Brochetas'),
                    ('empanadas_cocktail', 'Empanadas Cocktail'),
                ]
            # Agrega más condiciones para cada opción en tipo_servicio_choices dentro de la condición 'cumpleaños'
        # Agrega más condiciones para cada opción en tipos_eventos_choices
        
        super().save(*args, **kwargs)


class Cotizacion(models.Model):
    nroCotizacion = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Numero de la Cotizacion')
    nombreCotizacion = models.CharField(max_length=100,verbose_name='Nombre de la Cotizacion')
    rutCliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, max_length=9, verbose_name='RUT del Cliente')

    def __str__(self):
        return self.nombreCotizacion


class DetalleCotizacion(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE, verbose_name='Numero de la Cotizacion')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default='')

    def subtotal(self):
        return self.cantidad * self.servicio.precioServicio
    
    def nombre_cotizacion(self):
        return self.cotizacion.nombreCotizacion



class Evento(models.Model):
    idEvento = models.IntegerField(primary_key=True, verbose_name='ID del Evento')
    fechaEvento = models.DateField(verbose_name='Fecha del Evento')
    cantPersonas = models.IntegerField(verbose_name='Cantidad de Personas del Evento')
    imgEvento = models.ImageField(upload_to="productos", null=True, verbose_name='Imagen del Evento')
    nroCotizacion = models.ForeignKey(Cotizacion, on_delete=models.PROTECT, default='', verbose_name='Numero de la Cotizacion')
    
    def __str__(self):
        return self.idEvento


opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre= models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    rutCliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, max_length=9, verbose_name='RUT del Cliente')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default='')

    def subtotal(self):
        return self.cantidad * self.producto.precioProducto
    