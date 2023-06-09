# Generated by Django 4.2 on 2023-06-29 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0024_alter_producto_descproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebSE.producto')),
                ('rutCliente', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.PROTECT, to='WebSE.cliente', verbose_name='RUT del Cliente')),
            ],
        ),
    ]
