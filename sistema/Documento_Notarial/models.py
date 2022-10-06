from django.db import models
from Tipo_Doc_Notarial.models import Tipo_Doc_Notarial
from Consulta.models import Consulta

# Create your models here.

select_estado = (

    ('I', 'Iniciado'),
    ('P','En proceso'),
    ('S', 'En pausa'),
    ('F', 'Finalizado'),
    ('E', 'Entregado'),
    ('C', 'Cancelado'),
)

class Documento_Notarial(models.Model):
    idDocumento_Notarial = models.AutoField( primary_key=True)
    link = models.URLField(null=True, blank=True)
    estado = models.CharField('Estado', max_length=1, choices=select_estado,
                                  help_text='Seleccione el estado')
    idTipo_Doc_Notarial = models.ForeignKey(Tipo_Doc_Notarial, on_delete=models.CASCADE)
    idConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    class Meta():
        db_table = 'documento notarial'
        verbose_name = 'Documento Notarial'
        verbose_name_plural = 'Documentos Notariales'