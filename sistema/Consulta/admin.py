from django.contrib import admin
from Consulta.models import Consulta

# Register your models here.

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['motivo', 'fechaInicio', 'idCliente', 'estado']
    list_filter = ['motivo', 'idCliente']
    search_fields = ['motivo']

admin.site.register(Consulta, ConsultaAdmin)