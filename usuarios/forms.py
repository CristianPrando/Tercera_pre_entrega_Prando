from django import forms
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm

class Formulario_alta_usuario(forms.Form):

  usuario = forms.CharField(max_length=20)
  contrasenia = forms.CharField(max_length=20, widget=forms.PasswordInput)

  def clean_contrasenia(self):
        contrasenia = self.cleaned_data.get('contrasenia')
        if len(contrasenia) > 8:
            raise forms.ValidationError("La contraseña no puede tener más de 8 caracteres.")
        return contrasenia
  
  def clean_usuario(self):
        usuario = self.cleaned_data.get('usuario')
        if Usuario.objects.filter(usuario=usuario).exists():
            raise forms.ValidationError("El nombre de usuario ya existe. Por favor, elige otro.")
        return usuario