# Generated by Django 4.1.1 on 2022-09-23 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Recordatorio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinatario',
            fields=[
                ('idDestinatario', models.AutoField(primary_key=True, serialize=False)),
                ('destino', models.CharField(help_text='Ingresa el destinatario', max_length=30, verbose_name='Destinatario')),
                ('idRecordatorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recordatorio.recordatorio')),
            ],
            options={
                'verbose_name': 'Destinatario',
                'verbose_name_plural': 'Destinatarios',
                'db_table': 'destinatario',
            },
        ),
    ]
