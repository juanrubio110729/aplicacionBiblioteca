# Generated by Django 4.2 on 2023-06-26 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_autor_primer_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2023, 6, 29, 11, 7, 34, 789075), verbose_name='Fecha de devolucion'),
        ),
    ]