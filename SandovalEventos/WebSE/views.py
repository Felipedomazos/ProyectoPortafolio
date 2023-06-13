from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages, auth
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.views.generic import DeleteView
from django.urls import reverse_lazy
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
    rut_cliente = request.session.get('cliente_rut')
    cotizaciones = Cotizacion.objects.filter(rutCliente=rut_cliente)
    context = {
        'cotizaciones': cotizaciones
    }
    return render(request, 'Matrimonio.html', context)

def Celebracion(request):
    return render(request, 'Celebracion.html')

def Tabla(request):
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProducto')
        descProducto = request.POST.get('descProducto')
        cantPersonas = request.POST.get('cantPersonas')
        precioProducto = request.POST.get('precioProducto')
        imagenProducto = request.FILES.get('imagenProductos')

        objeto = Producto(nombreProducto=nombreProducto, descProducto=descProducto, precioProducto=precioProducto, cantPersonas=cantPersonas, imagenProducto=imagenProducto)
        objeto.save()
        
    objetos = Producto.objects.filter(nombreProducto__icontains='Tabla')
    print(objetos)

    return render(request, 'Tablas.html', {'objetos': objetos})

def Desayuno(request):
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProducto')
        descProducto = request.POST.get('descProducto')
        cantPersonas = request.POST.get('cantPersonas')
        precioProducto = request.POST.get('precioProducto')
        imagenProducto = request.FILES.get('imagenProductos')

        objeto = Producto(nombreProducto=nombreProducto, descProducto=descProducto, precioProducto=precioProducto, cantPersonas=cantPersonas, imagenProducto=imagenProducto)
        objeto.save()
        
    objetos = Producto.objects.filter(nombreProducto__icontains='Desayuno')
    print(objetos)

    return render(request, 'Desayunos.html', {'objetos': objetos})

def Registro(request):
    if request.method == 'POST':
        rutCliente = request.POST['rut']
        nombreCliente = request.POST['nombre']
        apellidoCliente = request.POST['apellido']
        fonoCliente = request.POST['phone']
        correoCliente = request.POST['email']
        contraseñaCliente = request.POST['password']
        
        cliente = Cliente(rutCliente=rutCliente, nombreCliente=nombreCliente, apellidoCliente=apellidoCliente, fonoCliente=fonoCliente, correoCliente=correoCliente, contraseñaCliente=contraseñaCliente)
        cliente.save()
        
        return redirect('login')  # Redirige a la página del formulario después de guardar los datos

    return render(request, 'Registro.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            cliente = Cliente.objects.get(correoCliente=email)

            if cliente.contraseñaCliente == password:
                # Las credenciales son válidas, iniciar sesión
                request.session['cliente_nombre'] = f"{cliente.nombreCliente} {cliente.apellidoCliente}"
                request.session['cliente_rut'] = cliente.rutCliente
                print(request.session.items())
                return redirect('Inicio')  # Redirecciona a la página de inicio después del inicio de sesión exitoso
            else:
                # La contraseña no coincide
                messages.error(request, 'Contraseña incorrecta.')
        except Cliente.DoesNotExist:
            # El cliente no existe
            messages.error(request, 'El correo electrónico no está registrado.')
    
    return render(request, 'Login.html')

def Cuenta(request):
    if 'cliente_nombre' in request.session:
        cliente_nombre = request.session['cliente_nombre']
        nombre_completo = cliente_nombre.split()
        if len(nombre_completo) == 2:
            nombre = nombre_completo[0]
            apellido = nombre_completo[1]
            try:
                cliente = Cliente.objects.get(nombreCliente=nombre, apellidoCliente=apellido)
                return render(request, 'Cuenta.html', {'cliente': cliente})
            except Cliente.DoesNotExist:
                return redirect('Inicio')
        else:
            return redirect('Inicio')
    else:
        return redirect('Inicio')

def actualizar_cliente(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        fono = request.POST['fono']
        direccion = request.POST['direccion']
        contraseña = request.POST['contraseña']

        cliente = Cliente.objects.get(rutCliente=rut)

        cliente.nombreCliente = nombre
        cliente.apellidoCliente = apellido
        cliente.correoCliente = correo
        cliente.fonoCliente = fono
        cliente.direccionCliente = direccion
        cliente.contraseñaCliente = contraseña

        cliente.save()

        return redirect('Inicio')

    return render(request, 'Cuenta.html')

def cerrar_sesion(request):
    auth.logout(request)
    return redirect('Inicio')

def Administracion(request):
    clientes = Cliente.objects.all()
    return render(request, 'Administracion.html', {'clientes': clientes})

def adminTablas(request, producto_id=None):
    if producto_id:
        producto = get_object_or_404(Producto, idProducto=producto_id)
    else:
        producto = None
        
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProducto')
        descProducto = request.POST.get('descProducto')
        cantPersonas = request.POST.get('cantPersonas')
        precioProducto = request.POST.get('precioProducto')
        imagenProducto = request.FILES.get('imagenProductos')

        objeto = Producto(nombreProducto=nombreProducto, descProducto=descProducto, precioProducto=precioProducto, cantPersonas=cantPersonas, imagenProducto=imagenProducto)
        objeto.save()

    objetos = Producto.objects.filter(nombreProducto__icontains='Tabla')

    context = {
        'producto': producto,
        'objetos': objetos
    }

    return render(request, 'adminTablas.html', context)

def adminDesayunos(request, producto_id=None):
    if producto_id:
        producto = get_object_or_404(Producto, idProducto=producto_id)
    else:
        producto = None
        
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProducto')
        descProducto = request.POST.get('descProducto')
        cantPersonas = request.POST.get('cantPersonas')
        precioProducto = request.POST.get('precioProducto')
        imagenProducto = request.POST.get('imagenProductos')

        objeto = Producto(nombreProducto=nombreProducto, descProducto=descProducto, precioProducto=precioProducto, cantPersonas=cantPersonas, imagenProducto=imagenProducto)
        objeto.save()

    objetos = Producto.objects.filter(nombreProducto__icontains='Desayuno')

    context = {
        'producto': producto,
        'objetos': objetos
    }

    return render(request, 'adminDesayunos.html', context)

def Cotizaciones(request):
    if request.method == 'POST':
        nombre_cotizacion = request.POST['nombre_cotizacion']
        rut_cliente = request.session.get('cliente_rut')
        cliente = Cliente.objects.get(rutCliente=rut_cliente)
        cotizacion = Cotizacion(nombreCotizacion=nombre_cotizacion, rutCliente=cliente)
        cotizacion.save()
        messages.success(request, 'La cotización se ha creado exitosamente. ')
        return redirect('cotizaciones')
    
    rutcliente = request.session.get('cliente_rut')
    cotizaciones = Cotizacion.objects.filter(rutCliente=rutcliente)
    context = {
        'cotizaciones': cotizaciones
    }

    return render(request, 'Cotizaciones.html', context)

class EliminarObjeto(DeleteView):
    model = Producto
    success_url = reverse_lazy('administracion')

class EliminarCliente(DeleteView):
    model = Cliente
    success_url = reverse_lazy('administracion')