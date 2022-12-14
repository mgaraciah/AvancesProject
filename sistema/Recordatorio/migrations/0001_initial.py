# Generated by Django 4.1.1 on 2022-09-23 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Consulta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recordatorio',
            fields=[
                ('idRecordatorio', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(help_text='Ingresa el titulo', max_length=15, verbose_name='Titulo')),
                ('motivo', models.CharField(help_text='Ingresa el Motivo', max_length=15, verbose_name='Motivo')),
                ('horaRecordatorio', models.DateTimeField(auto_now_add=True, verbose_name='Hora Recordatorio')),
                ('fechaRecordatorio', models.DateTimeField(auto_now_add=True, verbose_name='Fecha REcordatorio')),
                ('finalizado', models.CharField(help_text='Finzalizado', max_length=15, verbose_name='Finalizado')),
                ('idConsulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Consulta.consulta')),
            ],
            options={
                'verbose_name': 'Recordatorio',
                'verbose_name_plural': 'Recordatorios',
                'db_table': 'recordatorio',
            },
        ),
    ]
