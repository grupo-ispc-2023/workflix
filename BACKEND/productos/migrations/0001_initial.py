# Generated by Django 4.2.1 on 2023-06-18 17:45

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import usuarios.common


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, max_length=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10, max_length=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('imagen', models.ImageField(null=True, upload_to='images', verbose_name='imagen')),
                ('cantidad', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'verbose_name': 'Articulos del negocio',
                'verbose_name_plural': 'Articulos',
                'db_table': 'Articulo',
            },
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(validators=[usuarios.common.aceptar_solo_fechas_futuras])),
                ('comprado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Carrito de compra',
                'verbose_name_plural': 'Carritos',
                'db_table': 'Carrito',
            },
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10, max_length=10, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
            ],
            options={
                'verbose_name': 'Tipos de envios disponibles',
                'verbose_name_plural': 'Envios',
                'db_table': 'Envio',
            },
        ),
        migrations.CreateModel(
            name='TipoArticulo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Tipos de articulos disponibles',
                'verbose_name_plural': 'TipoArticulos',
                'db_table': 'TipoArticulo',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.PositiveIntegerField()),
                ('comprobante', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(validators=[usuarios.common.aceptar_solo_fechas_pasadas])),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, max_length=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.carrito')),
                ('envio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.envio')),
            ],
            options={
                'verbose_name': 'Listado de Ventas',
                'verbose_name_plural': 'Ventas',
                'db_table': 'Venta',
            },
        ),
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.articulo')),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.carrito')),
            ],
            options={
                'verbose_name': 'Seleccion de articulos',
                'verbose_name_plural': 'Selecciones',
                'db_table': 'Seleccion',
            },
        ),
    ]
