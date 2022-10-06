from django.db import models
from Recordatorio.models import Recordatorio

# Create your models here.

class Destinatario(models.Model):
    idDestinatario = models.AutoField(primary_key=True)
    destino = models.CharField('Destinatario', max_length=30, help_text='Ingresa el destinatario')
    idRecordatorio = models.ForeignKey(Recordatorio, on_delete=models.CASCADE, verbose_name = 'Id Recordatorio')

    
    class Meta():
        db_table = 'destinatario'
        verbose_name = 'Destinatario'
        verbose_name_plural = 'Destinatarios'