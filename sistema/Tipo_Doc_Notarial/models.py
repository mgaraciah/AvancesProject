from django.db import models

# Create your models here.

class Tipo_Doc_Notarial(models.Model):
    idTipo_Doc_Notarial = models.AutoField(primary_key=True)
    tipo_documento = models.CharField('Tipo de Documento', max_length=15, help_text='Ingresa el Tipo')

    def __str__(self):
        return "%s" %(self.tipo_documento)

    class Meta():
        db_table = 'tipo_de_documento'
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'