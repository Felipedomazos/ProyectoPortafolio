# Generated by Django 4.2 on 2023-05-29 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imgProducto',
        ),
    ]
