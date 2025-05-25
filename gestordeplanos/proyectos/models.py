from django.db import models

# Create your models here.
class Proyecto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ruta = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
