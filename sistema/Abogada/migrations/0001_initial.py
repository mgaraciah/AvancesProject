# Generated by Django 4.1.1 on 2022-09-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abogada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese Nombre', max_length=30, verbose_name='Nombre')),
                ('apelllido', models.CharField(help_text='Ingrese Apellido', max_length=30, verbose_name='Apellido')),
                ('telefono', models.BigIntegerField(blank=True, help_text='Ingrese Número de Teléfono', null=True, verbose_name='Teléfono')),
                ('colegiado', models.BigIntegerField(blank=True, help_text='Ingrese Colegiado', null=True, verbose_name='Colegiado')),
                ('correo', models.CharField(help_text='Ingrese Correo Electrónico', max_length=50, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Abogada',
                'db_table': 'abogada',
            },
        ),
    ]
