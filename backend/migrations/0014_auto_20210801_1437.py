# Generated by Django 3.1.7 on 2021-08-01 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20210801_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='ids',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='files',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 1, 14, 37, 37, 561060)),
        ),
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
