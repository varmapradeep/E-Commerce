# Generated by Django 4.1 on 2024-01-06 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_Location',
            fields=[
                ('Locationid', models.AutoField(primary_key=True, serialize=False)),
                ('Locationname', models.CharField(max_length=50)),
            ],
        ),
    ]