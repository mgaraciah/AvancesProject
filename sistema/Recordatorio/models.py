from django.db import models
from Consulta.models import Consulta

# Create your models here.

select_genero = (

    ('S','Si'),
    ('N', 'No'),
)

class Recordatorio(models.Model):
    idRecordatorio = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=200, help_text='Ingresa el titulo')
    motivo = models.CharField('Motivo', max_length=200, help_text='Ingresa el Motivo')
    horaRecordatorio = models.DateTimeField('Hora Recordatorio', auto_now_add=True)
    fechaRecordatorio = models.DateTimeField('Fecha Recordatorio', auto_now_add=True)
    finalizado = models.CharField('Finalizado', max_length=1, choices=select_genero, default='M',
      help_text='Seleccione si esta finalizado o no')
    idConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, verbose_name = 'Consulta')

    class Meta():
        db_table = 'recordatorio'
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'