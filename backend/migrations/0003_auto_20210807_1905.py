# Generated by Django 3.1.7 on 2021-08-07 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210807_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 19, 5, 37, 481230)),
        ),
        migrations.AlterField(
            model_name='like',
            name='like_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 19, 5, 37, 518132)),
        ),
    ]