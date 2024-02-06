from django.db import models

from ADMIN.models import Tbl_Subcategory
from Guest.models import Tbl_Seller, Login


# Create your models here.
class Tbl_Product(models.Model):
    objects = None
    Productid = models.AutoField(primary_key=True)
    Sellerid = models.ForeignKey(Login, on_delete=models.CASCADE)
    Subcategoryid = models.ForeignKey(Tbl_Subcategory, on_delete=models.CASCADE)
    Productname = models.CharField(max_length=50)
    Productdesc = models.CharField(max_length=1000)
    Productprice = models.BigIntegerField()
    ProductStock = models.BigIntegerField()
    productimage1 = models.ImageField()
    productimage2 = models.ImageField()
    Productregdate = models.DateField(auto_now_add=True)
