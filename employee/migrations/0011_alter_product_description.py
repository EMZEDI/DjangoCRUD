# Generated by Django 4.0.1 on 2022-01-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_remove_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='Quantity = 1, Date added:2022-01-12'),
        ),
    ]