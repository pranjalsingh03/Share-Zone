# Generated by Django 3.1.7 on 2021-07-31 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20210731_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='files',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 31, 18, 36, 50, 999879)),
        ),
    ]