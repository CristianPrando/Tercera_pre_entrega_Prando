from django import forms
from .models import Usuario

class Formulario_alta_usuario(forms.Form):

  usuario = forms.CharField(max_length=20)
  contrasenia = forms.CharField(max_length=20, widget=forms.PasswordInput)
  profesional = forms.BooleanField(required=False)

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
  
class Formulario_crear_perfil(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    matricula = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()
    biografia = forms.CharField(widget=forms.Textarea, required=False)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email