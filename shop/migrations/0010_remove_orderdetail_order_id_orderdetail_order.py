# Generated by Django 4.0.6 on 2022-08-01 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0009_remove_orderdetail_product_id_orderdetail_products"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderdetail",
            name="order_id",
        ),
        migrations.AddField(
            model_name="orderdetail",
            name="order",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="shop.order",
                verbose_name="Order",
            ),
            preserve_default=False,
        ),
    ]
