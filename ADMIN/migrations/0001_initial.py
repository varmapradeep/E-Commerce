# Generated by Django 4.1 on 2024-01-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_District',
            fields=[
                ('Districtid', models.AutoField(primary_key=True, serialize=False)),
                ('Districtname', models.CharField(max_length=50)),
            ],
        ),
    ]