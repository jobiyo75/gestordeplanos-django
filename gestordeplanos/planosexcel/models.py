from django.db import models

# Create your models here.
class PlanoExcel(models.Model):
    numero = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    paquete = models.CharField(max_length=100)
    hoja = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.numero} - {self.nombre}"