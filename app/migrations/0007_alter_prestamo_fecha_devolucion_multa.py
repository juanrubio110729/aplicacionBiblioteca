# Generated by Django 4.2 on 2023-06-26 13:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_alter_prestamo_fecha_devolucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2023, 6, 29, 8, 57, 27, 331105), verbose_name='Fecha de devolucion'),
        ),
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(blank=True, null=True, verbose_name='Valor multa')),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descripcion Multa')),
                ('fecha', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Multa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Multas',
                'db_table': 'multa',
            },
        ),
    ]