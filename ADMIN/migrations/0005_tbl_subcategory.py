# Generated by Django 4.1 on 2024-01-18 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN', '0004_tbl_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_Subcategory',
            fields=[
                ('Subcategoryid', models.AutoField(primary_key=True, serialize=False)),
                ('Subcategoryname', models.CharField(max_length=50)),
                ('Subcategorydesc', models.CharField(max_length=100)),
                ('Subcategoryimg', models.ImageField(upload_to='')),
                ('Categoryid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ADMIN.tbl_category')),
            ],
        ),
    ]