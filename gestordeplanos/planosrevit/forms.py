from django import forms

class CargarCSVRevitForm(forms.Form):
    archivo_csv = forms.FileField(label="Selecciona archivo CSV")
