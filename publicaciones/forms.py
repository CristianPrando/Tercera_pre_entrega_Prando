from django import forms


class Formulario_crear_publicacion(forms.Form):
    
    titulo = forms.CharField(max_length=100)
    categoria = forms.CharField(max_length=100)
    texto = forms.CharField(widget=forms.Textarea, required=False)
