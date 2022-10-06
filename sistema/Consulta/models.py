from django.db import models
from Cliente.models import Cliente
from Abogada.models import Abogada
from Secretaria.models import Secretaria

# Creación del Modelo Consulta.

class Consulta(models.Model):
    idConsulta = models.AutoField(primary_key=True)
    motivo = models.CharField('Motivo', max_length=15, help_text='Ingresa el Motivo')
    fechaInicio = models.DateTimeField('Fecha Inicio', db_column='Fecha Inicio')
    faFin = models.DateTimeField('Fecha Fin', db_column='Fecha Fin')
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='DPI Cliente')
    idColegiado = models.ForeignKey(Abogada, on_delete=models.CASCADE, verbose_name='ID Colegiado')
    dpiSecre = models.ForeignKey(Secretaria, on_delete=models.CASCADE, verbose_name='DPI Secretaria')#agregar al principio los verbose

    def __str__(self):
        return "%s %s" %(self.idCliente, self.motivo)

    class Meta():
        db_table = 'consulta'
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'