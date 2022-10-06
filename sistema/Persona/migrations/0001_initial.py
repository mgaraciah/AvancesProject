# Generated by Django 4.1.1 on 2022-09-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese Nombre', max_length=30, verbose_name='Nombre')),
                ('apelllido', models.CharField(help_text='Ingrese Apellido', max_length=30, verbose_name='Apellido')),
                ('telefono', models.BigIntegerField(blank=True, help_text='Ingrese Teléfono', null=True, verbose_name='Teléfono')),
            ],
        ),
    ]
