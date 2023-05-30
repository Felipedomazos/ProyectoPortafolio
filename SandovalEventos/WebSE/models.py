from django.db import models
import uuid

# Create your models here.

class Cliente(models.Model):
    rutCliente = models.IntegerField(primary_key=True, verbose_name='RUT del Cliente')
    nombreCliente = models.CharField(max_length=20, verbose_name='Nombre del Cliente')
    apellidoCliente = models.CharField(max_length=20, verbose_name='Apellido del Cliente')
    correoCliente = models.EmailField(max_length=40, verbose_name='Correo del Cliente')
    fonoCliente = models.IntegerField(verbose_name='Fono del Cliente')
    direccionCliente = models.CharField(max_length=50, verbose_name='Direccion del Cliente')

    class Meta:
        ordering = ["apellidoCliente"]

    def __str__(self):
        return self.nombreCliente


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
    descProducto = models.CharField(max_length=60,verbose_name='Descripcion del Producto')
    cantPersonas = models.IntegerField(verbose_name='Cantidad de Personas Maximas para el producto', default='0')
    precioProducto = models.IntegerField(verbose_name='Precio del Producto')
    imagenProducto = models.ImageField(upload_to='img/', default='0')

    def __str__(self):
        return self.nombreProducto


class Evento(models.Model):
    idEvento = models.IntegerField(primary_key=True, verbose_name='ID del Evento')
    fechaEvento = models.DateField(verbose_name='Fecha del Evento')
    cantPersonas = models.IntegerField(verbose_name='Cantidad de Personas del Evento')
    imgEvento = models.ImageField(upload_to="productos", null=True, verbose_name='Imagen del Evento')
    def __str__(self):
        return self.idEvento


class Cotizacion(models.Model):
    nroCotizacion = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Numero de la Cotizacion')
    nombreCotizacion = models.CharField(max_length=100,verbose_name='Nombre de la Cotizacion')
    rutCliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, max_length=9, verbose_name='RUT del Cliente')
    idEvento = models.ForeignKey(Evento, on_delete=models.PROTECT, max_length=2, verbose_name='ID del Evento')

    def __str__(self):
        return self.nroCotizacion


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