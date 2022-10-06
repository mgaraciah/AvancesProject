from django.db import models
from Tipo_Doc_Notarial.models import Tipo_Doc_Notarial
from Consulta.models import Consulta

# Create your models here.

class Documento_Notarial(models.Model):
    idDocumento_Notarial = models.AutoField( primary_key=True)
    link = models.URLField(null=True, blank=True)
    idTipo_Doc_Notarial = models.ForeignKey(Tipo_Doc_Notarial, 
                on_delete=models.CASCADE, verbose_name='Tipo de Documento Notarial')
    idConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, verbose_name='Consulta')

    class Meta():
        db_table = 'documento notarial'
        verbose_name = 'Documento Notarial'
        verbose_name_plural = 'Documentos Notariales'