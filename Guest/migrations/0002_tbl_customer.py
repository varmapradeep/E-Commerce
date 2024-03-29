# Generated by Django 4.1 on 2024-01-16 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_Customer',
            fields=[
                ('Customerid', models.AutoField(primary_key=True, serialize=False)),
                ('Customername', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=30)),
                ('Gender', models.CharField(max_length=20)),
                ('Phone', models.BigIntegerField()),
                ('Housename', models.CharField(max_length=30)),
                ('pincode', models.BigIntegerField()),
                ('Customerimage', models.ImageField(upload_to='')),
                ('Loginid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Guest.login')),
            ],
        ),
    ]
