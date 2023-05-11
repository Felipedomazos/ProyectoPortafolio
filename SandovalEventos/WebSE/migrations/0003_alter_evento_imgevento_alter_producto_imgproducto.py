# Generated by Django 4.0.5 on 2023-05-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0002_evento_imgevento_producto_imgproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imgEvento',
            field=models.ImageField(null=True, upload_to='productos', verbose_name='Imagen del Evento'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imgProducto',
            field=models.ImageField(null=True, upload_to='productos', verbose_name='Imagen del Producto'),
        ),
    ]
