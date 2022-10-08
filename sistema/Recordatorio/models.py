from django.db import models
from Consulta.models import Consulta
from django.utils.html import format_html

# Create your models here.

select_estado = (

    ('Y','Si esta finalizado'),
    ('S', 'Sin completar'),
    ('R', 'Revisión'),
)

class Recordatorio(models.Model):
    idRecordatorio = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=200, help_text='Ingresa el titulo')
    motivo = models.CharField('Motivo', max_length=200, help_text='Ingresa el Motivo')
    estado = models.CharField('Estado', max_length=1, choices=select_estado, default='M',
      help_text='Seleccione si esta finalizado, en revisón, sin completar')
    idConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, verbose_name = 'Consulta')

    def __str__(self):
        return "%s %s" %(self.idConsulta.idCliente.nombre, self.idConsulta.idCliente.apellido,)

    def consulta1_(self):
        nombre = self.idConsulta.idCliente.nombre
        apellido = self.idConsulta.idCliente.apellido
        return "%s %s" %(nombre,apellido)
    consulta1_.short_description = 'Nombre Cliente'
    consulta1_.allow_tags = True

    def motivo1_(self):
        motivo = self.idConsulta.motivo
        return "%s" %(motivo)
    motivo1_.short_description = 'Motivo de Consulta'
    motivo1_.allow_tags = True

    def proceso1_(self):

        if self.estado == 'Y':
           return format_html('<img src="/media/pngegg(04).png" height="35" width="35">')
        if self.estado == 'S':
           return format_html('<img src="/media/pngegg(05).png" height="35" width="35">')
        else:
            return format_html('<img src="/media/pngegg(03).png" height="35" width="35">')
    proceso1_.short_description = 'Estado 2'
    proceso1_.allow_tags = True

    class Meta():
        db_table = 'recordatorio'
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'