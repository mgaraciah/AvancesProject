# Generated by Django 4.1.1 on 2022-10-08 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recordatorio', '0005_alter_recordatorio_finalizado_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recordatorio',
            options={'verbose_name': 'Agenda', 'verbose_name_plural': 'Agendas'},
        ),
    ]
