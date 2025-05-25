# filepath: c:\Users\PO3\Documents\JVG\15-VSC\VSC\gigafactoria\mis_funciones.py
import pandas as pd


# FUCTION LEER_EXCEL
#-------------------------------
"""
    Lee un archivo Excel y devuelve un DataFrame filtrado por columnas deseadas.
    
    :param file_path: Ruta del archivo Excel.
    :param sheet_name: Nombre de la hoja a leer.
    :return: DataFrame filtrado o mensaje de error.
    """

def leer_excel(file_path, sheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl", dtype=str)
        columnas_deseadas = ['Recuento planos_SD','Building Number_SD','Número_SD', 'Nombre_SD', 'Nombre de Archivo_SD', 'Paquete_SD']
        if all(col in df.columns for col in columnas_deseadas):
            df_filtrado = df[columnas_deseadas]
            # Eliminar filas donde 'Nombre' es NaN
            df_filtrado = df_filtrado.dropna(subset=['Nombre_SD'])
            return df_filtrado
        else:
            return "Alguna columna no existe en el archivo."

    except FileNotFoundError:
        return 'El archivo no se encontró. Verifica la ruta y el nombre del archivo.'

    except Exception as e:
        return f"ERROR: {e}"

# TEST
#---------------------------
#file_path_excel = r"..\data\FCI-BIM-TM-MIDP_WIP.xlsx"
#sheet_name_excel = "02 MEP Electrical"
#file_path_excel = r"..\data\Libro1.xlsx"
#sheet_name_excel = "Hoja1"

#df_excel = leer_excel(file_path_excel, sheet_name_excel) # return DataFrame
#valores_paquete = df_excel['Paquete_SD'].value_counts().to_dict()
#print(df_excel)
#---------------------------



# FUCTION LEER_CSV
#-------------------------------
"""
    Lee un archivo csv y devuelve un DataFrame filtrado por columnas deseadas.
    
    :param file_path: Ruta del archivo Excel.
    :param sheet_name: Nombre de la hoja a leer.
    :return: DataFrame filtrado o mensaje de error.
    """

def leer_csv(file_path):
    try:
        df = pd.read_csv(file_path, sep=';', dtype=str)
        return df

    except FileNotFoundError:
        return 'El archivo no se encontró. Verifica la ruta y el nombre del archivo.'

    except Exception as e:
        return f"ERROR: {e}"

#That's all floks!