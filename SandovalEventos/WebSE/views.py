from django.shortcuts import render
from .forms import ContactoForm
from .models import Producto, Cliente, Pedido, DetallePedido, Evento, Cotizacion, Contacto

# Create your views here.


def Inicio(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Enviado!"
        else:
            data["form"] = formulario

    return render(request, 'Inicio.html', data)

def Matrimonio(request):
    return render(request, 'Matrimonio.html')

def Celebracion(request):
    return render(request, 'Celebracion.html')

def Tabla(request):
    return render(request, 'Tablas.html')

def Desayuno(request):
    return render(request, 'Desayunos.html')

def Registro(request):
    return render(request, 'Registro.html')

def Administracion(request):
    return render(request, 'Administracion.html')

def adminTablas(request):
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProducto')
        descProducto = request.POST.get('descProducto')
        cantPersonas = request.POST.get('cantPersonas')
        precioProducto = request.POST.get('precioProducto')
        imagenProducto = request.POST.get('imagenProductos')

        objeto = Producto(nombreProducto=nombreProducto, descProducto=descProducto, precioProducto=precioProducto, cantPersonas=cantPersonas, imagenProducto=imagenProducto)
        objeto.save()
        
    datos = Producto.objects.all()
    print(datos)

    return render(request, 'AdminTablas.html', {'datos': datos})
