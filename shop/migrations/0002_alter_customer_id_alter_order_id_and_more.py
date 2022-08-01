# Generated by Django 4.0.6 on 2022-08-01 12:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.UUIDField(default=uuid.UUID('018378c9-d6bf-42ae-a261-eab23053115d'), editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('018378c9-d6bf-42ae-a261-eab23053115d'), editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='id',
            field=models.UUIDField(default=uuid.UUID('018378c9-d6bf-42ae-a261-eab23053115d'), editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('018378c9-d6bf-42ae-a261-eab23053115d'), editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
