# Generated by Django 4.2 on 2023-07-03 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0034_alter_carrito_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='servicios',
        ),
    ]
