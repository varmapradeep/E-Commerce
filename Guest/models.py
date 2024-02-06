from django.db import models

from ADMIN.models import Tbl_Location


# Create your models here.
class Login(models.Model):
    objects = None
    Loginid = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Role = models.CharField(max_length=15)
    Status = models.CharField(max_length=15)


class Tbl_Customer(models.Model):
    objects = None
    Customerid = models.AutoField(primary_key=True)
    Customername = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    Gender = models.CharField(max_length=20)
    locationid = models.ForeignKey(Tbl_Location, on_delete=models.CASCADE)
    Phone = models.BigIntegerField()
    Regdate = models.DateField(auto_now_add=True)
    Housename = models.CharField(max_length=30)
    pincode = models.BigIntegerField()
    Loginid = models.ForeignKey(Login, on_delete=models.CASCADE)
    Customerimage = models.ImageField()


class Tbl_Seller(models.Model):
    objects = None
    Sellerid = models.AutoField(primary_key=True)
    Sellername = models.CharField(max_length=25)
    Selleremail = models.CharField(max_length=30)
    SellerGender = models.CharField(max_length=20)
    locationid = models.ForeignKey(Tbl_Location, on_delete=models.CASCADE)
    SellerPhone = models.BigIntegerField()
    Regdate = models.DateField(auto_now_add=True)
    Housename = models.CharField(max_length=30)
    pincode = models.BigIntegerField()
    Loginid = models.ForeignKey(Login, on_delete=models.CASCADE)
    Sellerimage = models.ImageField()
    Idproof = models.ImageField()
