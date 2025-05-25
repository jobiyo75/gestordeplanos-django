#--------------------------------
# PLANOSREVIT/VIEWS.PY
#--------------------------------

from django.shortcuts import render
from .models import PlanoRevit
from .forms import CargarCSVRevitForm
from django.core.paginator import Paginator

import pandas as pd


#--------------------------------
# importar_form.html
#--------------------------------
def importar_csv_revit(request):
    mensaje=''
    if request.method == 'POST':
        form = CargarCSVRevitForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo_csv']

            # Leer csv con pandas
            try:
                df = pd.read_csv(archivo, delimiter=';', encoding='utf-8')
            except Exception as e:
                mensaje = f'Error al leer el archivo: {e}'
                return render(request, 'planosrevit/importar_form.html', {'form': form, 'mensaje': mensaje})

        planos_creados = 0
        planos_actualizados = 0
        planos_omitidos = 0

        for _, fila in df.iterrows():
            sheetnumber = str(fila.get('Sheet Number', '')).strip()

            if not sheetnumber:
                continue

            sheetname = str(fila.get('Sheet Name', '')).strip()
            viewsubgroup = str(fila.get('GEN_ViewSubgroup', '')).strip()
            buildingzone = str(fila.get('SHE_DisciplineBuildingZone', '')).strip()

            plano, creado = PlanoRevit.objects.update_or_create(
                sheetnumber=sheetnumber,
                defaults={
                    'sheetname': sheetname,
                    'viewsubgroup': viewsubgroup,
                    'buildingzone': buildingzone,
                }
            )

            if creado:
                planos_creados += 1
            else:
                planos_actualizados +=1
        
        mensaje = (
            f"{planos_creados} planos creados, "
            f"{planos_actualizados} actualizados correctamente."
        )

    else:
        form = CargarCSVRevitForm()

    return render(request, 'planosrevit/importar_form.html',{'form': form, 'mensaje': mensaje})



#--------------------------------
# lista_planos_revit.html
#--------------------------------
def lista_planos_revit(request):
    consulta = request.GET.get('q', '').strip()
    viewsubgroup_filtrado = request.GET.get('viewsubgroup', '')

    planos_revit = PlanoRevit.objects.all()

    if consulta:
        planos_revit = planos_revit.filter(sheetname__icontains=consulta)
    
    if viewsubgroup_filtrado:
        planos_revit = planos_revit.filter(viewsubgroup=viewsubgroup_filtrado)
    
    planos_revit = planos_revit.order_by('sheetname')
    viewsubgroups_unicos = PlanoRevit.objects.values_list('viewsubgroup', flat=True).distinct().order_by('viewsubgroup')

    paginator = Paginator(planos_revit, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'consulta': consulta,
        'viewsubgroup_filtrado': viewsubgroup_filtrado,
        'viewsubgroups': viewsubgroups_unicos
    }


    return render(request, 'planosrevit/lista_planos_revit.html', context)