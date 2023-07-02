# Generated by Django 4.2.2 on 2023-07-01 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mesa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_mesa", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("precio", models.DecimalField(decimal_places=3, max_digits=8)),
                ("cantidad", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Registro_ventas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=100)),
                ("cantidad_v", models.IntegerField(blank=True)),
                (
                    "monto",
                    models.DecimalField(decimal_places=3, default=0, max_digits=8),
                ),
                ("fecha", models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Venta_mesa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad_vendida", models.IntegerField()),
                (
                    "monto_mesa",
                    models.DecimalField(decimal_places=3, default=0, max_digits=8),
                ),
                ("fecha_venta", models.DateField()),
                (
                    "mesaId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="inventory.mesa"
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.producto",
                    ),
                ),
            ],
        ),
    ]
