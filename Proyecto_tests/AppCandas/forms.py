from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Moto_formulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    estado = forms.CharField(max_length=40)
    año = forms.IntegerField()
    precio = forms.IntegerField()

class Repuesto_formulario(forms.Form):
    item = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    precio = forms.IntegerField()

class Sucursal_formulario(forms.Form):
    provincia = forms.CharField(max_length=40)
    localidad = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    telefono = forms.IntegerField()





class usereditform (UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}



