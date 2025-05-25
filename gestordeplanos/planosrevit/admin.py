from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import PlanoRevit

# Register your models here.
class PlanoRevitResource(resources.ModelResource):
    class Meta:
        model = PlanoRevit
        import_id_fields = ['sheetnumber']
        fields = ('sheetnumber', 'sheetname', 'viewsubgroup', 'buildingzone')


@admin.register(PlanoRevit)
class PlanoRevitAdmin(admin.ModelAdmin):
    list_display = ('sheetnumber', 'sheetname', 'viewsubgroup', 'buildingzone')
    search_fields = ('sheetnumber', 'sheetname', 'buildingzone')
    list_filter = ('viewsubgroup', 'buildingzone',)
    ordering = ('sheetnumber',)
