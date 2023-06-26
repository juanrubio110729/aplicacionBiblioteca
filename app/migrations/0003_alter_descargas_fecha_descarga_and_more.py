# Generated by Django 4.2 on 2023-06-26 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_prestamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descargas',
            name='fecha_descarga',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de descarga'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='ejemplar',
            field=models.ManyToManyField(to='app.ejemplar', verbose_name='Ejemplares'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2023, 6, 29, 7, 42, 43, 296605), verbose_name='Fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_realizacion',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de realizacion'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de solicitud'),
        ),
    ]
