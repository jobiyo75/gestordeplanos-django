# filepath: gestordeplanos/core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_auth/', views.home_auth, name='home_auth'),
    path('about/', views.about, name='about'),
    path('contact/', views.contacto, name='contact'),
    path('mensajes/', views.list_contacts, name='mensajes'),
    path('logout/', views.logout_view, name='logout'),

    path('list_excel/', views.list_excel, name='list_excel'),
    path('paquete/<str:nombre_paquete>/', views.filtar_paquete, name='filtrar_paquete'),  # URL para filtrar por paquete

    path('list_csv/', views.list_csv, name='list_csv'),
    path('viewsubgroup/<str:nombre_viewsubgroup>/', views.filtrar_viewsubgroup, name='filtrar_viewsubgroup'),  # URL para filtrar por viewsubgroup
    ]