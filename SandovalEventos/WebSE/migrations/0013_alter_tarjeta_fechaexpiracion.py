# Generated by Django 4.2 on 2023-06-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0012_tarjeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='fechaExpiracion',
            field=models.CharField(max_length=7, verbose_name='Fecha de Expiración (MM/YY)'),
        ),
    ]