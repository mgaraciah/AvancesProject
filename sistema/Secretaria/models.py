from django.db import models
from Persona.models import Persona

# Create your models here.

class Secretaria(Persona):
    dpiSecre = models.CharField('DPI de Secretaria', max_length=20, help_text='Ingrese DPI')
    direccion = models.CharField('Dirección', max_length=50, help_text='Ingrese Dirección')

    class Meta():
        db_table = 'secretaria'
        verbose_name = 'Secretaria'
