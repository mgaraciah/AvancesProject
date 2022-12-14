from django.contrib import admin
from Recordatorio.models import Recordatorio

# Register your models here.

class RecordatorioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'motivo', 'consulta1_', 'motivo1_', 'estado', 'proceso1_']
    list_filter = ['titulo', 'idConsulta']
    search_fields = ['titulo']

admin.site.register(Recordatorio, RecordatorioAdmin)