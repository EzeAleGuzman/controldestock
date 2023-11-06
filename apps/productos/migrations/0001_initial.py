# Generated by Django 4.2.7 on 2023-11-06 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('stock', models.PositiveIntegerField()),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=7)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=5)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
            ],
        ),
    ]