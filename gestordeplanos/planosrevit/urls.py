from django.urls import path
from . import views

urlpatterns = [
    path('importar/', views.importar_csv_revit, name='importar_planos_revit'),
    path('listado/', views.lista_planos_revit, name='lista_planos_revit'),
]