# Generated by Django 4.0.5 on 2023-05-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='imgEvento',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imgProducto',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
