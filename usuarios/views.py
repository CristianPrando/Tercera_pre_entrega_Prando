from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def inicio(req):
    return render(req, 'inicio.html', {})

def nuevo_usuario(req):
    if req.method == 'POST':
        crear_usuario = Formulario_alta_usuario(req.POST)
        if crear_usuario.is_valid():
            data = crear_usuario.cleaned_data
            nuevousuario = Usuario(
                usuario=data["usuario"],
                contrasenia=data["contrasenia"]
            )
            nuevousuario.save()
            return render(req, "Saludonuevousuario.html", {"usuario": data["usuario"]})
        else:
            return render(req, "nuevo_usuario.html", {"crear_usuario": crear_usuario})
    else:
        crear_usuario = Formulario_alta_usuario()
        return render(req, "nuevo_usuario.html", {"crear_usuario": crear_usuario})

def iniciar_sesion(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        
        try:
            usuario = Usuario.objects.get(usuario=username)
            if usuario.contrasenia == password:
                
                return render(req, 'Post_inicio_sesion.html', {}) 
            else:
                messages.error(req, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(req, 'Usuario no encontrado.')
        
        return render(req, 'iniciar_sesion.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(req, 'iniciar_sesion.html')
def Post_inicio_sesion(req):
    return render(req, 'Post_inicio_sesion.html', {})

def SobreNosotros(req):
    return render(req, 'Sobre_nosotros.html', {})

def crear_perfil(req):
    if req.method == 'POST':
        crear_perfil_form = Formulario_crear_perfil(req.POST)
        if crear_perfil_form.is_valid():
            data = crear_perfil_form.cleaned_data
            nuevo_perfil = Perfil(
                nombre=data["nombre"],
                apellido=data["apellido"],
                email=data["email"],
                biografia=data["biografia"],
            )
            nuevo_perfil.save()
            return render(req, "mostrar_perfil.html", {"usuario": data["nombre"]})
        else:
            return render(req, "crear_perfil.html", {"crear_perfil_form": crear_perfil_form})
    else:
        crear_perfil_form = Formulario_crear_perfil()
        return render(req, "crear_perfil.html", {"crear_perfil_form": crear_perfil_form})

def mostrar_perfil(req, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)
    return render(req, 'mostrar_perfil.html', {'perfil': perfil})

def buscar_perfil(req):

  prof = req.GET["apellido"]

  nombre = Perfil.objects.filter(apellido__icontains=prof)

  return render(req, "resultado_busqueda.html", { "nombre": nombre, "apellido": prof})