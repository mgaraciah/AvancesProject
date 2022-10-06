from pyexpat import model
from django.contrib import admin
from Cliente.models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'dpicliente', 'direccion', 'genero', 'nit', 'estadocivil']
    list_filter = ['nombre', 'apellido']
    search_fields = ['nombre', 'dpicliente']

admin.site.register(Cliente, ClienteAdmin)