# Generated by Django 4.1 on 2024-01-06 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN', '0002_tbl_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_location',
            name='Districtid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ADMIN.tbl_district'),
        ),
    ]