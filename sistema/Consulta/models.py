from django.db import models
from Cliente.models import Cliente
from Abogada.models import Abogada
from Secretaria.models import Secretaria

# Creación del Modelo Consulta.

select_estado = (

    ('I', 'Iniciado'),
    ('P','En proceso'),
    ('S', 'En pausa'),
    ('F', 'Finalizado'),
    ('E', 'Entregado'),
    ('C', 'Cancelado'),
)

class Consulta(models.Model):
    idConsulta = models.AutoField(primary_key=True)
    motivo = models.CharField('Motivo', max_length=200, help_text='Ingresa el Motivo')
    fechaInicio = models.DateTimeField('Fecha Inicio', db_column='Fecha Inicio')
    faFin = models.DateTimeField('Fecha Fin', db_column='Fecha Fin')
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    estado = models.CharField('Estado', max_length=1, choices=select_estado,
                                  help_text='Seleccione el estado')
    idColegiado = models.ForeignKey(Abogada, on_delete=models.CASCADE, verbose_name='ID Colegiado')
    dpiSecre = models.ForeignKey(Secretaria, on_delete=models.CASCADE, verbose_name='DPI Secretaria')#agregar al principio los verbose

    def __str__(self):
        return "%s %s" %(self.idCliente, self.motivo)

    class Meta():
        db_table = 'consulta'
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'