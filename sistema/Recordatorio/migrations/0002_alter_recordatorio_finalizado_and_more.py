# Generated by Django 4.1.1 on 2022-09-28 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Consulta', '0004_alter_consulta_dpisecre_alter_consulta_idcliente_and_more'),
        ('Recordatorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordatorio',
            name='finalizado',
            field=models.CharField(help_text='Ingrese si esta finzalizado el recordatorio', max_length=15, verbose_name='Finalizado'),
        ),
        migrations.AlterField(
            model_name='recordatorio',
            name='idConsulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Consulta.consulta', verbose_name='Id Consulta'),
        ),
    ]
