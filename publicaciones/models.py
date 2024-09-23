from django.db import models
from usuarios.models import Perfil, Usuario

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    texto = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    apellido = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.apellido}'