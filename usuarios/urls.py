"""
URL configuration for Tercera_preentrega_Prando project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from publicaciones.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('nuevo_usuario/', nuevo_usuario, name='nuevo_usuario'),
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('buscar_usuario/', buscar_usuario, name='buscar_usuario'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('Sobrenosotros/', SobreNosotros, name='SobreNosotros'),
    path('Comencemos/', Post_inicio_sesion, name='Comencemos'),
    path('crear_perfil/', crear_perfil, name='crear_perfil'),
    path('lista_profesionales/', lista_profesionales, name='lista_profesionales'),
    path('buscar_profesionales/', buscar_profesionales, name='buscar_profesionales'),
    path('crear_publicacion', crear_publicacion, name='crear_publicacion'),
    path('buscar_publicacion/', buscar_publicacion, name='buscar_publicacion'),
    path('lista_publicaciones/', lista_publicaciones, name='lista_publicaciones'),
    path('psicoanalisis', psicoanalisis, name='psicoanalisis'),
    path('sistemica', sistemica, name='sistemica'),
    path('cognitivoconductual', cognitivo_conductual, name='cognitivoconductual'),
    path('clinica', clinica, name='clinica'),
    ]