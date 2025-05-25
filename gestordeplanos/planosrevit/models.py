from django.db import models

# Create your models here.
class PlanoRevit(models.Model):
    sheetnumber = models.CharField(max_length=100)
    sheetname = models.CharField(max_length=100)
    viewsubgroup = models.CharField(max_length=100)
    buildingzone = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.sheetnumber} - {self.sheetname}'
