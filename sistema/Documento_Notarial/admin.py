from django.contrib import admin
from Documento_Notarial.models import Documento_Notarial

# Register your models here.

class Documento_NotarialAdmin(admin.ModelAdmin):
    list_display = ['link', 'idTipo_Doc_Notarial', 'idConsulta']
    list_filter = ['idTipo_Doc_Notarial']
    search_fields = ['idConsulta']

admin.site.register(Documento_Notarial, Documento_NotarialAdmin)