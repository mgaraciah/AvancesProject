from django.db import models
from Cliente.models import Cliente
from Abogada.models import Abogada
from Secretaria.models import Secretaria
from django.utils.html import format_html
# Creación del Modelo Consulta.

select_estado = (

    ('I', 'Iniciado'),
    ('P','En proceso'),
    ('S', 'En pausa'),
    ('F', 'Finalizado'),
    ('E', 'Entregado'),
    ('C', 'Cancelado'),
)

select_tipo_persona = (

    ('S', 'Secretaria'),
    ('A','Abogada'),
)

class Consulta(models.Model):
    idConsulta = models.AutoField(primary_key=True)
    motivo = models.CharField('Motivo', max_length=200, help_text='Ingresa el Motivo')
    fechaInicio = models.DateTimeField('Fecha Inicio', db_column='Fecha Inicio')
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    estado = models.CharField('Estado', max_length=1, choices=select_estado,
                                  help_text='Seleccione el estado')
    tipo_persona = models.CharField('Tipo de Persona', max_length=1, choices=select_tipo_persona,
                                  help_text='Seleccione el tipo de Persona')

    def __str__(self):
        return "%s %s" %(self.idCliente, self.motivo)


    def proceso_(self):

        if self.estado == 'I':
           return format_html('<img src="/media/pngegg(1).png" height="35" width="35">')
        if self.estado == 'P':
           return format_html('<img src="/media/pngegg(2).png" height="35" width="35">')
        if self.estado == 'S':
           return format_html('<img src="/media/pngegg(3).png" height="35" width="35">')
        if self.estado == 'E':
           return format_html('<img src="/media/pngegg(5).png" height="35" width="35">')
        if self.estado == 'C':
           return format_html('<img src="/media/pngegg(6).png" height="35" width="35">')
        else:
            return format_html('<img src="/media/pngegg.png" height="35" width="35">')
    proceso_.short_description = 'Estado 2'
    proceso_.allow_tags = True


    class Meta():
        db_table = 'consulta'
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'