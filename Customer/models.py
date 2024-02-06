from django.db import models

from Guest.models import Login
from Seller.models import Tbl_Product


# Create your models here.

class Tbl_cart(models.Model):
    objects = None
    Cartid = models.AutoField(primary_key=True)
    Productid = models.ForeignKey(Tbl_Product, on_delete=models.CASCADE)
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE)
    Quantity = models.BigIntegerField()
    Cartdate = models.DateField()
    Status = models.CharField(max_length=30)

