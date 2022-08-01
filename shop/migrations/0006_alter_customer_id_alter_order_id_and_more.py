# Generated by Django 4.0.6 on 2022-08-01 12:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_customer_id_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.UUIDField(default=uuid.UUID('95bccb1b-02e6-446f-a099-34ea54093717'), editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('95bccb1b-02e6-446f-a099-34ea54093717'), editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='id',
            field=models.UUIDField(default=uuid.UUID('95bccb1b-02e6-446f-a099-34ea54093717'), editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('95bccb1b-02e6-446f-a099-34ea54093717'), editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
