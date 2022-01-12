import datetime

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(max_length=20, default=1.99)

    class Meta:
        db_table = "product"
