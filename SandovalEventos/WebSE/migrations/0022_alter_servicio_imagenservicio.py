# Generated by Django 4.2 on 2023-06-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0021_alter_servicio_imagenservicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagenServicio',
            field=models.ImageField(blank=True, default='none', upload_to='img/'),
        ),
    ]