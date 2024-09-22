from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def inicio(req):
    return render(req, 'inicio.html', {})

def nuevo_usuario(req):
    
    if req.method == 'POST':

        crear_usuario = Formulario_alta_usuario(req.POST)

        if crear_usuario.is_valid():

            data = crear_usuario.cleaned_data

            nuevousuario = Usuario(usuario=data["usuario"], contrasenia=data["contrasenia"])
            nuevousuario.save()

            return render(req, "inicio.html", {})
    
        else:
            return render(req, "nuevo_usuario.html", { "crear_usuario": crear_usuario })
  
    else:

        crear_usuario = Formulario_alta_usuario()
        return render(req, "nuevo_usuario.html", { "crear_usuario": crear_usuario })

def iniciar_sesion(req):
    pass