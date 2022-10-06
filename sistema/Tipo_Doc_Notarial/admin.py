from django.contrib import admin
from Tipo_Doc_Notarial.models import Tipo_Doc_Notarial

# Register your models here.

class Tipo_Doc_NotarialAdmin(admin.ModelAdmin):
    list_display = ['tipo_documento']
    search_fields = ['tipo_documento']

admin.site.register(Tipo_Doc_Notarial, Tipo_Doc_NotarialAdmin)