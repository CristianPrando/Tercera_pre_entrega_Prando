from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def inicio(req):
    return render(req, 'inicio.html', {})

def SobreNosotros(req):
    return render(req, 'Sobre_nosotros.html', {})

def nuevo_usuario(req):
    if req.method == 'POST':
        crear_usuario = Formulario_alta_usuario(req.POST)
        if crear_usuario.is_valid():
            data = crear_usuario.cleaned_data
            nuevousuario = Usuario(
                usuario=data["usuario"],
                contrasenia=data["contrasenia"],
                profesional=data["profesional"]
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
                matricula=data["matricula"],
            )
            nuevo_perfil.save()
            return render(req, "perfilcreado.html", {"usuario": data["nombre"]})
        else:
            return render(req, "crear_perfil.html", {"crear_perfil_form": crear_perfil_form})
    else:
        crear_perfil_form = Formulario_crear_perfil()
        return render(req, "crear_perfil.html", {"crear_perfil_form": crear_perfil_form})

def lista_profesionales(req):
    perfiles = Perfil.objects.all()
    return render(req, 'lista_profesionales.html', {'perfiles': perfiles})

def buscar_profesionales(req):
    query = req.GET.get('q')
    if query:
        perfiles = Perfil.objects.filter(apellido__icontains=query)
    else:
        perfiles = Perfil.objects.all()
    return render(req, 'buscar_profesional.html', {'perfiles': perfiles})

def lista_usuarios(req):
    usuarios = Usuario.objects.all()
    return render(req, 'lista_usuarios.html', {'usuarios': usuarios})

def buscar_usuario(req):
    query = req.GET.get('q')
    if query:
        usuario = Usuario.objects.filter(usuario__icontains=query)
    else:
        usuario = Usuario.objects.all()
    return render(req, 'buscar_usuario.html', {'usuarios': usuario})

def psicoanalisis(req):
    return render(req, 'psicoanalisis.html', {})

def clinica(req):
    return render(req, 'clinica.html', {})

def cognitivo_conductual(req):
    return render(req, 'cognitivoconductual.html', {})

def sistemica(req):
    return render(req, 'sistemica.html', {})

