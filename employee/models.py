import datetime

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Quantity = 1, Date added:' + str(datetime.date.today()))
    price = models.FloatField(max_length=20, default=1.99)

    class Meta:
        db_table = "product"
