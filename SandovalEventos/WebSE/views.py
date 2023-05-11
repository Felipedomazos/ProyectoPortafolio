from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


def Inicio(request):
    return render(request, 'Inicio.html')
def Matrimonio(request):
    return render(request, 'Matrimonio.html')
def Celebracion(request):
    return render(request, 'Celebracion.html')
def Tabla(request):
    return render(request, 'Tablas.html')
def Desayuno(request):
    return render(request, 'Desayunos.html')