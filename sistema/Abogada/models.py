from tabnanny import verbose
from django.db import models
from Persona.models import Persona

# Creación de Modelo Abogada.


class Abogada(Persona): # Clase Abogada que hereda los atributos de la clase persona.
    colegiado = models.CharField('Colegiado', max_length=20, help_text= 'Ingresa Colegiado', primary_key=True)
    correo = models.CharField('Correo', max_length=50, help_text='Ingrese Correo Electrónico')

    class Meta():
        db_table = 'abogada'
        verbose_name = 'Abogada'