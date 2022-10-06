# Generated by Django 4.1.1 on 2022-10-06 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0006_rename_apelllido_cliente_apellido_and_more'),
        ('Consulta', '0007_alter_consulta_motivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente', verbose_name='Cliente'),
        ),
    ]