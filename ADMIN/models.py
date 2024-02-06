from django.db import models


# Create your models here.
class Tbl_District(models.Model):
    objects = None
    Districtid = models.AutoField(primary_key=True)
    Districtname = models.CharField(max_length=50)


class Tbl_Location(models.Model):
    objects = None
    Locationid = models.AutoField(primary_key=True)
    Locationname = models.CharField(max_length=50)
    Districtid = models.ForeignKey(Tbl_District, on_delete=models.CASCADE, default="")


class Tbl_Category(models.Model):
    objects = None
    Categoryid = models.AutoField(primary_key=True)
    Categoryname = models.CharField(max_length=50)
    Categorydesc = models.CharField(max_length=100)
    Categoryimg = models.ImageField()


class Tbl_Subcategory(models.Model):
    objects = None
    Subcategoryid = models.AutoField(primary_key=True)
    Categoryid = models.ForeignKey(Tbl_Category, on_delete=models.CASCADE, default="")
    Subcategoryname = models.CharField(max_length=50)
    Subcategorydesc = models.CharField(max_length=100)
    Subcategoryimg = models.ImageField()
