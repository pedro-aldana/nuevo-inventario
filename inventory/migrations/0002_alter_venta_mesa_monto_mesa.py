# Generated by Django 4.2.2 on 2023-07-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venta_mesa",
            name="monto_mesa",
            field=models.DecimalField(
                blank=True, decimal_places=3, default=0, max_digits=8
            ),
        ),
    ]
