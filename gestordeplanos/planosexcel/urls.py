from django.urls import path
from . import views

urlpatterns = [
    path('importar/', views.importar_planos_excel, name='importar_planos_excel'),
    path('listado/', views.lista_planos_excel, name='lista_planos_excel'),
    path('comparar/', views.comparar_planos, name='comparar_planos'),
]