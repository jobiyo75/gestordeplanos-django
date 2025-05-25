# PROYECTOS/ADMIN.PY
from django.contrib import admin
from .models import Proyecto

# Register your models here.
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo',)




