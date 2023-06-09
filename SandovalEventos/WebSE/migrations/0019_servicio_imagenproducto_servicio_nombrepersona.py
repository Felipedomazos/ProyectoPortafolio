# Generated by Django 4.2 on 2023-06-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0018_alter_servicio_precioservicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagenProducto',
            field=models.ImageField(default='0', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='nombrePersona',
            field=models.CharField(default='', max_length=100, verbose_name='Nombre de quien imparte el servicio'),
        ),
    ]
