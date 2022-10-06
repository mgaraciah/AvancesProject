from django.db import models
from Persona.models import Persona

# Create your models here.

select_genero = (

    ('M','Masculino'),
    ('F', 'Femenino'),
)

select_estadocivil = (

    ('S','Soltero'),
    ('C', 'Casado'),
    ('V', 'Viudo'),
)

class Cliente(Persona):
    dpicliente = models.CharField('DPI de Cliente', max_length=20, help_text= 'Ingresa DPI', primary_key=True)
    direccion = models.CharField('Dirección', max_length=50, help_text='Ingresar Dirección')
    genero = models.CharField('Genero', max_length=1, choices=select_genero, default='M',
                                  help_text='Seleccione su genero')
    nit = models.CharField('Nit', max_length=15, help_text='Ingrese Nit')
    estadocivil = models.CharField('Estado Civil', max_length=1, choices=select_estadocivil,
                                  help_text='Seleccione Estado Civil')

    class Meta():
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'