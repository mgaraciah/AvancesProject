# Generated by Django 4.1.1 on 2022-10-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0005_alter_cliente_genero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='apelllido',
            new_name='apellido',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estadocivil',
            field=models.CharField(choices=[('S', 'Soltero'), ('C', 'Casado'), ('V', 'Viudo')], help_text='Seleccione Estado Civil', max_length=1, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', help_text='Seleccione su genero', max_length=1, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(help_text='Ingrese Número de Teléfono', max_length=15, verbose_name='Teléfono'),
        ),
    ]
