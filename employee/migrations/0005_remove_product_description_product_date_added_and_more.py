# Generated by Django 4.0.1 on 2022-01-10 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_product_description_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='num',
            field=models.IntegerField(default=1),
        ),
    ]