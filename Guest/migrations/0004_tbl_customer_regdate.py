# Generated by Django 4.1 on 2024-01-20 09:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_tbl_customer_locationid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_customer',
            name='Regdate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]