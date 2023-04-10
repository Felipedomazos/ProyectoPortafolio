from django.db import models
import uuid

# Create your models here.

class Cliente(models.Model):
    rutCliente = models.IntegerField(primary_key=True, max_length=9, verbose_name='RUT del Cliente')
    nombreCliente = models.CharField(max_length=20, verbose_name='Nombre del Cliente')
    apellidoCliente = models.CharField(max_length=20, verbose_name='Apellido del Cliente')
    correoCliente = models.EmailField(max_length=40, verbose_name='Correo del Cliente')
    fonoCliente = models.IntegerField(max_length=9, verbose_name='Fono del Cliente')
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
    idPedido = models.ForeignKey(verbose_name='ID del Pedido')
    idProducto = models.ForeignKey(verbose_name='ID del Producto')
    rutCliente = models.ForeignKey(max_length=9, verbose_name='RUT del Cliente')

    def __str__(self):
        return self.idPedido


class Producto(models.Model):
    idProducto = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='ID del Producto')
    nombreProducto = models.CharField(verbose_name='Nombre del Producto')
    descProducto = models.CharField(verbose_name='Descripcion del Producto')
    precioProducto = models.IntegerField(verbose_name='Precio del Producto')

    def __str__(self):
        return self.idProducto


class Evento(models.Model):
    idEvento = models.IntegerField(primary_key=True, max_length=2, verbose_name='ID del Evento')
    fechaEvento = models.DateField(verbose_name='Fecha del Evento')
    cantPersonas = models.IntegerField(verbose_name='Cantidad de Personas del Evento')

    def __str__(self):
        return self.idEvento


class Cotizacion(models.Model):
    nroCotizacion = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Numero de la Cotizacion')
    nombreCotizacion = models.CharField(verbose_name='Nombre de la Cotizacion')
    rutCliente = models.ForeignKey(max_length=9, verbose_name='RUT del Cliente')
    idEvento = models.ForeignKey(max_length=2, verbose_name='ID del Evento')

    def __str__(self):
        return self.nroCotizacion

