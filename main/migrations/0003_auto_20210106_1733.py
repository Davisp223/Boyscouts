# Generated by Django 3.1 on 2021-01-06 22:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210106_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 22, 33, 38, 897200, tzinfo=utc)),
        ),
    ]