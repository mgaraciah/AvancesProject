# Generated by Django 4.1.1 on 2022-10-08 03:35

from django.db import migrations, models
import sistema.valida


class Migration(migrations.Migration):

    dependencies = [
        ('Documento_Notarial', '0005_documento_notarial_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento_notarial',
            name='link',
        ),
        migrations.RemoveField(
            model_name='documento_notarial',
            name='logo',
        ),
        migrations.AddField(
            model_name='documento_notarial',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='documentos/notariales', validators=[sistema.valida.validate_file_extension], verbose_name='Documento'),
        ),
    ]