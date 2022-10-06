# Generated by Django 4.1.1 on 2022-10-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recordatorio', '0002_alter_recordatorio_finalizado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordatorio',
            name='fechaRecordatorio',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Recordatorio'),
        ),
        migrations.AlterField(
            model_name='recordatorio',
            name='motivo',
            field=models.CharField(help_text='Ingresa el Motivo', max_length=50, verbose_name='Motivo'),
        ),
        migrations.AlterField(
            model_name='recordatorio',
            name='titulo',
            field=models.CharField(help_text='Ingresa el titulo', max_length=50, verbose_name='Titulo'),
        ),
    ]