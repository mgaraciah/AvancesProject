from django.contrib import admin
from Consulta.models import Consulta

# Register your models here.


class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['motivo', 'fechaInicio', 'idCliente', 'estado']
    search_fields = ['idCliente']

admin.site.register(Consulta, ConsultaAdmin)