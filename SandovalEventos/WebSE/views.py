from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm

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