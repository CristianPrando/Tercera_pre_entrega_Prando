from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def inicio(req):
    return render(req, 'inicio.html', {})

def crear_publicacion(req):
    if req.method == 'POST':
        crear_publicacion_form = Formulario_crear_publicacion(req.POST)
        if crear_publicacion_form.is_valid():
            data = crear_publicacion_form.cleaned_data
            nueva_publicacion = Publicacion(
                titulo=data["titulo"],
                categoria=data["categoria"],
                texto=data["texto"],
            )
            nueva_publicacion.save()
            return render(req, "publicacioncreada.html", {})
        else:
            return render(req, "crear_publicacion.html", {"crear_publicacion_form": crear_publicacion_form})
    else:
        crear_publicacion_form = Formulario_crear_publicacion()
        return render(req, "crear_publicacion.html", {"crear_publicacion_form": crear_publicacion_form})
    
def buscar_publicacion(req):
    query = req.GET.get('q')
    if query:
        publicaciones = Publicacion.objects.filter(titulo__icontains=query)
    else:
        publicaciones = Publicacion.objects.all()
    return render(req, 'lista_publicaciones.html', {'publicaciones': publicaciones})

def lista_publicaciones(req):
    publicaciones = Publicacion.objects.all()
    return render(req, 'lista_publicaciones.html', {'publicaciones': publicaciones})

def publicacioncreada(req):
    return render(req, 'publicacioncreada.html', {})