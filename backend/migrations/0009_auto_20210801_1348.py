# Generated by Django 3.1.7 on 2021-08-01 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20210731_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.IntegerField(default='1', primary_key=True, serialize=False)),
                ('likeno', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='files',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 1, 13, 48, 59, 337473)),
        ),
    ]
