from django import forms

class Formulario_alta_usuario(forms.Form):

  usuario = forms.CharField(max_length=12)
  ccontrasenia = forms.CharField(max_length=8, widget=forms.PasswordInput)