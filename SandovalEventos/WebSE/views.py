from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


def Inicio(request):
    return render(request, 'Inicio.html')