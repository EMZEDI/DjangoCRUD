# Generated by Django 4.0.1 on 2022-01-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_remove_product_description_product_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateField(),
        ),
    ]