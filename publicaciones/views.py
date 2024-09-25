from django.shortcuts import render
from .forms import Formulario_crear_publicacion
from .models import Publicacion
from django.http import HttpResponseRedirect
# Create your views here.

def inicio(req):
    return render(req, 'inicio.html', {})

# def crear_publicacion(req):
#     if req.method == 'POST':
#         crear_publicacion = Formulario_crear_publicacion(req.POST)
#         if crear_publicacion.is_valid():
#             data = crear_publicacion.cleaned_data
#             nueva_publicacion = Publicacion(
#                 titulo=data["titulo"],
#                 categoria=data["categoria"],
#                 texto=data["texto"],
#                 usuario=data["usuario"],
#                 apellido=data["apellido"],
#             )
#             nueva_publicacion.save()
#             return render(req, "publicacioncreada.html", {})
#         else:
#             return render(req, "crear_publicacion.html", {"crear_publicacion": crear_publicacion})
#     else:
#         crear_publicacion = Formulario_crear_publicacion()
#         return render(req, "crear_publicacion.html", {"crear_publicacion": crear_publicacion})

def crear_publicacion(req):

  if req.method == 'POST':

    mi_formulario = Formulario_crear_publicacion(req.POST)

    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data

      nueva_publicacion = Publicacion(titulo=data["titulo"], categoria=data["categoria"], texto=data["texto"], autor=data["autor"])
      nueva_publicacion.save()

      return render(req, "publicacioncreada.html", {})
    
    else:
      return render(req, "publicacion_formulario.html", { "mi_formulario": mi_formulario })
  
  else:

    mi_formulario = Formulario_crear_publicacion()
    return render(req, "publicacion_formulario.html", { "mi_formulario": mi_formulario })

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