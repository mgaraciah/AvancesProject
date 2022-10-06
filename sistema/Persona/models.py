# -- coding: utf-8 --
 
from django.db import models

# Creación del Modelo de Persona


class Persona (models.Model):
    nombre = models.CharField('Nombre', max_length=30, help_text='Ingrese Nombre')
    apelllido = models.CharField('Apellido', max_length=30, help_text='Ingrese Apellido')
    telefono = models.CharField('Teléfono', max_length=15, help_text='Ingrese Número de Teléfono')

    def __str__(self):
        return "%s %s" %(self.nombre, self.apelllido)

    class Meta:
        abstract=True


