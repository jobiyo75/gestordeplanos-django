# filepath: gestordeplanos/core/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import ContactoForm
from .models import Contacto

# For authentication
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

# from myfunctions.py import read_excel
from funciones.mis_funciones import leer_excel, leer_csv

#-----------------------
# DATA
#-----------------------
#file_path_excel = r".\data\FCI-BIM-TM-MIDP_WIP.xlsx"
#sheet_name_excel = "02 MEP Electrical"
file_path_excel = r".\data\Libro1.xlsx"
sheet_name_excel = "Hoja1"



# Create your views here.
# home.html
def home(request):
    return render(request, 'core/home.html')


# home_auth.html
@login_required
def home_auth(request):
    #df_excel = leer_excel(file_path, sheet_name) # return DataFrame
    # Valores de la columna "Paquete"
    #valores_paquete = result['Paquete'].unique().tolist()
    #valores_paquete = result['Paquete_SD'].value_counts().to_dict()
    #table_html = result.to_html(classes="table table-striped", index=False, border=0)
    salida = 'salida'
    return render(request, 'core/home_auth.html', {
        #'table': table_html,
        #'table': df_excel,
        #'nun_rows': len(df_excel),
        #'valores_paquete': valores_paquete
        'salida':salida
        })


# about.html
def about(request):
    return render(request, 'core/about.html')

# contact.html
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a inicio después de guardar
    else:
        form = ContactoForm()
    
    return render(request, 'core/contact.html', {'form': form})


# list_contacts.html
@login_required
def list_contacts(request):
    contactos = Contacto.objects.all().order_by('-id')
    return render(request, 'core/list_contacts.html', {'contacts': contactos})


# logout.html
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente!')
    return redirect('home')


# list_excel.html
def list_excel(request):
    file_path = file_path_excel
    sheet_name = sheet_name_excel

    df_excel = leer_excel(file_path, sheet_name) # return DataFrame
    valores_paquete = df_excel['Paquete_SD'].value_counts().to_dict()
    valores_ordenados = dict(sorted(valores_paquete.items(), key=lambda item: item[0]))

    table_html = df_excel.to_html(classes="table table-striped", index=False, border=0)

    return render(request, 'core/list_excel.html', {'tabla': table_html,
                                                  'num_rows': len(df_excel),
                                                'valores_paquete': valores_ordenados})


# filtrar_paquete.html
def filtar_paquete(request, nombre_paquete):
    file_path = r".\data\Libro1.xlsx"
    sheet_name = "Hoja1"
    df = leer_excel(file_path, sheet_name) # return DataFrame
    df_filtrado = df[df['Paquete_SD'] == nombre_paquete]
    table_html = df_filtrado.to_html(classes="table table-striped", index=False, border=0)
    return render(request, 'core/paquete.html', {
        'table': table_html,
        'paquete': nombre_paquete,
        'num_filas': len(df_filtrado)
    })


# list_csv.html
def list_csv(request):
    file_path = r".\data\sheetlist.csv"
    df_list = leer_csv(file_path) # return DataFrame
    list_html = df_list.to_html(classes="table table-striped", index=False, border=0)
    valores_viewsubgroup = df_list['GEN_ViewSubgroup'].value_counts().to_dict()
    return render(request, 'core/list_csv.html', {'lista': list_html,
                                                  'num_rows': len(df_list),
                                                  'valores_viewsubgroup': valores_viewsubgroup})


# filtrar_viewsubgroup.html
def filtrar_viewsubgroup(request, nombre_viewsubgroup):
    file_path = r".\data\sheetlist.csv"
    df = leer_csv(file_path) # return DataFrame
    df_filtrado = df[df['GEN_ViewSubgroup'] == nombre_viewsubgroup]
    table_html = df_filtrado.to_html(classes="table table-striped", index=False, border=0)
    return render(request, 'core/viewsubgroup.html', {
        'table': table_html,
        'viewsubgroup': nombre_viewsubgroup,
        'num_filas': len(df_filtrado)
    })