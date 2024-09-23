from django.shortcuts import render

# Create your views here.

def inicio(req):
    return render(req, 'inicio.html', {})

def crear_publicacion(req):
    return render(req, 'crear_publicacion.html', {})