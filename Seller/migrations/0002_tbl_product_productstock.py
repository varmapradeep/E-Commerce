# Generated by Django 4.1 on 2024-01-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_product',
            name='ProductStock',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
