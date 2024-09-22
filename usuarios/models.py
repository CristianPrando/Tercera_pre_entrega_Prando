from django.db import models


# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=20)
    contrasenia = models.CharField(max_length=20)

    def __str__(self):
        return self.usuario
    