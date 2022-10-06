from django.db import models
from Consulta.models import Consulta

# Create your models here.


class Recordatorio(models.Model):
    idRecordatorio = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=15, help_text='Ingresa el titulo')
    motivo = models.CharField('Motivo', max_length=15, help_text='Ingresa el Motivo')
    horaRecordatorio = models.DateTimeField('Hora Recordatorio', auto_now_add=True)
    fechaRecordatorio = models.DateTimeField('Fecha REcordatorio', auto_now_add=True)
    finalizado = models.CharField('Finalizado', max_length=15, help_text='Ingrese si esta finzalizado el recordatorio')
    idConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, verbose_name = 'Id Consulta')

    class Meta():
        db_table = 'recordatorio'
        verbose_name = 'Recordatorio'
        verbose_name_plural = 'Recordatorios'