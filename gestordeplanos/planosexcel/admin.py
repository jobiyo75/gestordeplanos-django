from django.contrib import admin
from .models import PlanoExcel

# Register your models here.
@admin.register(PlanoExcel)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nombre', 'paquete', 'hoja')
    search_fields = ('numero', 'nombre', 'paquete')
    list_filter = ('paquete',)