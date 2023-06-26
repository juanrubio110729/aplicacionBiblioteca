# Generated by Django 4.2 on 2023-06-26 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_librodigital_libro'),
    ]

    operations = [
        migrations.AddField(
            model_name='librodigital',
            name='libro',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.libro', verbose_name='Libro'),
        ),
    ]