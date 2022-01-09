from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=True)
    price = models.CharField(max_length=20)

    # eid = models.CharField(max_length=20)
    # ename = models.CharField(max_length=100)
    # eemail = models.EmailField()
    # econtact = models.CharField(max_length=15)

    class Meta:
        db_table = "product"
