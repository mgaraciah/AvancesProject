from django.db import models
from Tipo_Doc_Notarial.models import Tipo_Doc_Notarial
from Consulta.models import Consulta
from sistema.valida import validate_file_extension
from django.utils.html import format_html
# Create your models here.

class Documento_Notarial(models.Model):
    idDocumento_Notarial = models.AutoField( primary_key=True)
    documento= models.FileField('Documento',upload_to='documentos/notariales', validators=[validate_file_extension],
         blank=True, null=True, )
    idTipo_Doc_Notarial = models.ForeignKey(Tipo_Doc_Notarial, 
        on_delete=models.CASCADE, verbose_name='Tipo de Documento Notarial')
    idConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, verbose_name='Consulta')


    def __str__(self):
        return "%s %s" %(self.idConsulta.idCliente.nombre, self.idConsulta.idCliente.apellido,)


    def consulta_(self):
        nombre = self.idConsulta.idCliente.nombre
        apellido = self.idConsulta.idCliente.apellido
        return "%s %s" %(nombre,apellido)
    consulta_.short_description = 'Nombre Cliente'
    consulta_.allow_tags = True

    def motivo_(self):
        motivo = self.idConsulta.motivo
        return "%s" %(motivo)
    motivo_.short_description = 'Motivo de Consulta'
    motivo_.allow_tags = True


    def url_(self):
        if self.documento:
           return format_html('<img src="/media/pngegg(02).png" height="35" width="35">')
        else:
            return format_html('<img src="/media/pngegg(01).png" height="35" width="35">')
    url_.short_description = 'Documento Cargado'
    url_.allow_tags = True


    class Meta():
        db_table = 'documento notarial'
        verbose_name = 'Documento Notarial'
        verbose_name_plural = 'Documentos Notariales'