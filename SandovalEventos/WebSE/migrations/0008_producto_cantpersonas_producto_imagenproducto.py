# Generated by Django 4.2 on 2023-05-30 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0007_remove_producto_imgproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantPersonas',
            field=models.IntegerField(default='0', verbose_name='Cantidad de Personas Maximas para el producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagenProducto',
            field=models.ImageField(default='0', upload_to='img/'),
        ),
    ]
