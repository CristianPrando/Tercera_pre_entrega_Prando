from django import forms
from usuarios.models import Usuario, Perfil


class Formulario_crear_publicacion(forms.Form):
    
    titulo = forms.CharField(max_length=100)
    categoria = forms.CharField(max_length=100)
    texto = forms.CharField(widget=forms.Textarea, required=False)
    autor = forms.ModelChoiceField(queryset=Perfil.objects.all())  
