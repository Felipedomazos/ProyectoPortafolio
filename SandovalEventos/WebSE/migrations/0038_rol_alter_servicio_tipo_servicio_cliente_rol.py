# Generated by Django 4.2 on 2023-07-04 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebSE', '0037_alter_servicio_subtipo_servicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='servicio',
            name='tipo_servicio',
            field=models.CharField(choices=[('bar', 'Bar'), ('aperitivos', 'Aperitivos'), ('entrada', 'Entrada'), ('plato_principal', 'Plato Principal'), ('postre', 'Postre'), ('personal', 'Personal'), ('vajilla_cristaleria', 'Vajilla y Cristalería'), ('decoracion', 'Decoración'), ('torta', 'Torta'), ('catering', 'Catering'), ('juegos_inflables', 'Juegos Inflables'), ('arreglo_floral', 'Arreglo Floral'), ('etretenimiento', 'Entretenimiento'), ('transporte', 'Transporte')], default='bar', max_length=30),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WebSE.rol'),
        ),
    ]