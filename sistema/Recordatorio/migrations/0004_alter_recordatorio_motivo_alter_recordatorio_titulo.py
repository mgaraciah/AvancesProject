# Generated by Django 4.1.1 on 2022-10-06 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recordatorio', '0003_alter_recordatorio_fecharecordatorio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordatorio',
            name='motivo',
            field=models.CharField(help_text='Ingresa el Motivo', max_length=200, verbose_name='Motivo'),
        ),
        migrations.AlterField(
            model_name='recordatorio',
            name='titulo',
            field=models.CharField(help_text='Ingresa el titulo', max_length=200, verbose_name='Titulo'),
        ),
    ]
