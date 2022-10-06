from django.contrib import admin
from Recordatorio.models import Recordatorio

# Register your models here.

class RecordatorioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'motivo', 'horaRecordatorio', 'fechaRecordatorio', 'finalizado', 'idConsulta']
    list_filter = ['titulo', 'idConsulta']
    search_fields = ['titulo']

admin.site.register(Recordatorio, RecordatorioAdmin)