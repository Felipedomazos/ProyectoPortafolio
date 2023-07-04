from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages, auth
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.views.generic import DeleteView, DetailView
from django.urls import reverse_lazy
import json
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest
from .forms import ContactoForm, ServicioForm
from .models import Carrito, Producto, Cliente, Pedido, DetallePedido, DetalleCotizacion, Evento, Cotizacion, Contacto, Tarjeta, Servicio

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
    if request.method == 'POST':
        nombreServicio = request.POST.get('nombreServicio')
        nombrePersona = request.POST.get('nombrePersona')
        precioServicio = request.POST.get('precioServicio')
        tipo_evento = request.POST.get('tipo_evento')
        tipo_servicio = request.POST.get('tipo_servicio')
        subtipo_servicio = request.POST.get('subtipo_servicio')
        imagenServicio = request.FILES.get('imagenServicio')

        objeto = Servicio(nombreServicio=nombreServicio, nombrePersona=nombrePersona, precioServicio=precioServicio, tipo_evento=tipo_evento, tipo_servicio=tipo_servicio, subtipo_servicio=subtipo_servicio, imagenServicio=imagenServicio)
        objeto.save()

    objetos = Servicio.objects.filter(tipo_evento__icontains='Matrimonio')

    rut_cliente = request.session.get('cliente_rut')
    cotizaciones = Cotizacion.objects.filter(rutCliente=rut_cliente)

    context = {
        'cotizaciones': cotizaciones,
        'objetos': objetos
    }

    return render(request, 'Matrimonio.html', context)

def Celebracion(request):
    if request.method == 'POST':
        nombreServicio = request.POST.get('nombreServicio')
        nombrePersona = request.POST.get('nombrePersona')
        precioServicio = request.POST.get('precioServicio')
        tipo_evento = request.POST.get('tipo_evento')
        tipo_servicio = request.POST.get('tipo_servicio')
        subtipo_servicio = request.POST.get('subtipo_servicio')
        imagenServicio = request.FILES.get('imagenServicio')

        objeto = Servicio(nombreServicio=nombreServicio, nombrePersona=nombrePersona, precioServicio=precioServicio, tipo_evento=tipo_evento, tipo_servicio=tipo_servicio, subtipo_servicio=subtipo_servicio, imagenServicio=imagenServicio)
        objeto.save()

    objetos = Servicio.objects.filter(Q(tipo_evento__icontains='Cumpleaños') | Q(tipo_evento__icontains='Aniversario') | Q(tipo_evento__icontains='Fiesta'))

    rut_cliente = request.session.get('cliente_rut')
    cotizaciones = Cotizacion.objects.filter(rutCliente=rut_cliente)

    context = {
        'cotizaciones': cotizaciones,
        'objetos': objetos
    }

    return render(request, 'Celebracion.html', context)

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

def Nosotros(request):
    return render(request, 'Nosotros.html')

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

def adminMatrimonio(request, servicio_id=None):
    if servicio_id:
        servicio = get_object_or_404(Servicio, id=servicio_id)
    else:
        servicio = None

    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminMatrimonio')
    else:
        form = ServicioForm()

    objetos = Servicio.objects.filter(tipo_evento__icontains='Matrimonio')

    context = {
        'servicio': servicio,
        'objetos': objetos,
        'form': form
    }

    return render(request, 'AdminMatrimonio.html', context)

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

def CoffeeBreak(request):
    return render(request, 'CoffeeBreak.html')

def mostrarDetalle(request, producto_nombre):
    producto = Producto.objects.get(nombreProducto=producto_nombre)
    product_nom = producto_nombre[-4:]

    context = {
        'producto': producto,
        'product_nom': product_nom
    }

    return render(request, 'DetalleProducto.html', context)

def detalleCotizacion(request, cotizacion_nombre):
    cotizacion = get_object_or_404(Cotizacion, nombreCotizacion=cotizacion_nombre)
    coti_nom = cotizacion_nombre[-5:]
    cotizacion_items = DetalleCotizacion.objects.filter(cotizacion=cotizacion)
    total = sum(item.subtotal() for item in cotizacion_items)

    context = {
        'cotizacion': cotizacion,
        'cotizacion_items': cotizacion_items,
        'total': total,
        'coti_nom': coti_nom
    }

    return render(request, 'DetalleCotizacion.html', context)

def Carro(request):
    rut_cliente = request.session.get('cliente_rut')
    carrito_items = Carrito.objects.filter(rutCliente=rut_cliente)
    total = sum(item.subtotal() for item in carrito_items)

    context = {
        'carrito_items': carrito_items,
        'total': total,
    }

    return render(request, 'Carro.html', context)

@csrf_exempt
def agregar_al_carrito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('productId')
        quantity = data.get('quantity')
        
        # Obtener el producto basado en su ID (ajusta esto según tu modelo de Producto)
        producto = Producto.objects.get(idProducto=product_id)
        
        # Obtener el usuario actualmente autenticado (ajusta esto según tu configuración de autenticación)
        rut_cliente = request.session.get('cliente_rut')
        cliente = Cliente.objects.get(rutCliente=rut_cliente)
        
        carrito_item = Carrito.objects.filter(rutCliente=cliente, producto=producto).first()

        if carrito_item:
            carrito_item.cantidad += quantity
            carrito_item.save()
        else:
            carrito_item = Carrito(rutCliente=cliente, producto=producto, cantidad=quantity)
            carrito_item.save()
        
        response_data = {'success': True}
        return JsonResponse(response_data, status=200)
    else:
        response_data = {'success': False, 'message': 'Método no permitido'}
        return JsonResponse(response_data, status=405)

@csrf_exempt
def eliminar_del_carrito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('itemId')
        
        # Eliminar el elemento del carrito basado en el item_id
        carrito_item = Carrito.objects.get(producto_id=item_id)
        carrito_item.delete()

        # Devolver una respuesta JSON de éxito
        response_data = {'success': True}
        return JsonResponse(response_data, status=200)
    else:
        # Devolver una respuesta JSON de error si la solicitud no es POST
        response_data = {'success': False, 'message': 'Método no permitido'}
        return JsonResponse(response_data, status=405)

def detalleFacturacion(request):
    return render(request, 'DetalleFacturacion.html')

@csrf_exempt
def eliminar_servicio_cotizacion(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('itemId')

        cotizacion_item = DetalleCotizacion.objects.get(servicio=item_id)
        cotizacion_item.delete()

        response_data = {'success': True}
        return JsonResponse(response_data, status=200)
    else:
        response_data = {'success': False, 'message': 'Método no permitido'}
        return JsonResponse(response_data, status=405)

@csrf_exempt
def agregar_servicio_cotizacion(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        cotizacion_id = request.POST.get('cotizacion')
        nom_cotizacion = request.POST.get('nombre_cotizacion')
        nombre_servicio = request.POST.get('nombre_servicio')

        try:
            cotizacion = Cotizacion.objects.get(nroCotizacion=cotizacion_id)
            servicio = Servicio.objects.get(nombreServicio=nombre_servicio)

            servicios = DetalleCotizacion.objects.filter(cotizacion=cotizacion, servicio=servicio).first()

            if servicios:
                servicios.cantidad += int(cantidad)
                servicios.save()
            else:
                servicios = DetalleCotizacion(cotizacion=cotizacion, servicio=servicio, cantidad=cantidad)
                servicios.save()

            return JsonResponse({'success': 'Servicio agregado a la cotización con éxito.'})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'La cotización no existe.'})

    return JsonResponse({'error': 'Error al agregar el servicio a la cotización.'})

def eliminar_cotizacion(request):
    if request.method == "POST":
        nro_cotizacion = request.POST.get("eliminarCotizacion")
        rut_cliente = request.POST.get("cliente_rut")

        try:
            cotizacion = Cotizacion.objects.get(nroCotizacion=nro_cotizacion, rutCliente=rut_cliente)
            cotizacion.delete()
            return redirect("cotizaciones") 
        except Cotizacion.DoesNotExist:
            return HttpResponseBadRequest("La cotización no existe")
    else:
        return HttpResponseBadRequest("Solicitud no válida")

class EliminarObjeto(DeleteView):
    model = Producto
    success_url = reverse_lazy('administracion')

class EliminarCliente(DeleteView):
    model = Cliente
    success_url = reverse_lazy('administracion')

class EliminarServicio(DeleteView):
    model = Servicio
    success_url = reverse_lazy('administracion')