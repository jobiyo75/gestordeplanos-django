#--------------------------------
# PLANOSEXCEL/VIEWS.PY
#--------------------------------

from django.shortcuts import render

from planosexcel.models import PlanoExcel
from planosrevit.models import PlanoRevit

from django.conf import settings
from django.core.paginator import Paginator

import pandas as pd
import os


#--------------------------------
# vista importar_form.html
#--------------------------------
def importar_planos_excel(request):
    cantidad = 0
    error = None
    #archivo = os.path.join(settings.BASE_DIR, 'data', 'Libro1.xlsx')


    if request.method == 'POST' and request.FILES.get('archivo'):
        archivo = request.FILES['archivo']

        try:
            df = pd.read_excel(archivo, sheet_name='Hoja1', engine='openpyxl')

            for _, fila in df.iterrows():
                PlanoExcel.objects.get_or_create(
                    numero = str(fila['Numero_SD']),
                    nombre = str(fila['Nombre_SD']),
                    paquete = str(fila['Paquete_SD']),
                    hoja = str(fila['Recuento planos_SD']),
                )
            cantidad = len(df)

        except Exception as e:
            error = str(e)
    
    return render(request, 'planosexcel/importar_form.html', {
        'cantidad': cantidad,
        'error': error
        })


#--------------------------------
# vista lista_planos_excel.html
#--------------------------------
def lista_planos_excel(request):
    consulta = request.GET.get('q','')
    paquete_filtrado = request.GET.get('paquete','')

    planos_excel = PlanoExcel.objects.all()

    if consulta:
        planos_excel = planos_excel.filter(nombre__icontains=consulta)

    if paquete_filtrado:
        planos_excel = planos_excel.filter(paquete=paquete_filtrado)

    paquetes_unicos = PlanoExcel.objects.values_list('paquete', flat=True).distinct().order_by('paquete')

    paginator = Paginator(planos_excel, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'colsulta': consulta,
        'paquete_filtrado': paquete_filtrado,
        'paquetes': paquetes_unicos
    }

    return render(request, 'planosexcel/lista_planos_excel.html', context)


#--------------------------------
# vista comparar.html
#--------------------------------
def comparar_planos(request):
    # Valores unicos
    numeros_excel = set(PlanoExcel.objects.values_list('numero', flat=True))
    sheetnumbers_revit = set(PlanoRevit.objects.values_list('sheetnumber', flat=True))

    # no_coinciden
    no_coinciden = [n for n in numeros_excel if n not in sheetnumbers_revit]
    
    # diferencias
    en_excel_no_en_revit = numeros_excel - sheetnumbers_revit
    en_revit_no_en_excel = sheetnumbers_revit - numeros_excel

    context = {
        'en_excel_no_en_revit': en_excel_no_en_revit,
        'en_revit_no_en_excel': en_revit_no_en_excel,
        'total_excel': len(numeros_excel),
        'total_revit': len(sheetnumbers_revit),
        'no_coinciden': no_coinciden,
        'total_no_coinciden': len(no_coinciden),
    }

    return render(request, 'planosexcel/comparar.html', context)