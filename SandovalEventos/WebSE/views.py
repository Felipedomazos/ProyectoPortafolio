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
