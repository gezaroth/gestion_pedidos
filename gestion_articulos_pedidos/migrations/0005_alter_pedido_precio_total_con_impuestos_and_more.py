# Generated by Django 5.0.4 on 2024-04-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_articulos_pedidos', '0004_pedido_cantidad_articulos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='precio_total_con_impuestos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='precio_total_sin_impuestos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
