from django import forms
from .models import Contacto, Servicio


class ContactoForm(forms.ModelForm):
        class Meta:
                model = Contacto
                #fields = ["nombre", "apellido", "correo", "tipo_consulta", "mensaje"]
                fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'