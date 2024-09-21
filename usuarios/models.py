from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=12)
    contrasenia = models.IntegerField(max_length=8)

    def __str__(self):
        return self.usuario