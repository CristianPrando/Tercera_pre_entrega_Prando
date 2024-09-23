from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=20)
    contrasenia = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.usuario}'
    
class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    biografia = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'