# Generated by Django 4.2 on 2023-06-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0020_rename_imagenproducto_servicio_imagenservicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagenServicio',
            field=models.ImageField(upload_to='img/'),
        ),
    ]