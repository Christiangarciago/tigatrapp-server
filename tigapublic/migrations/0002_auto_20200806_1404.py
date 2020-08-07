# Generated by Django 2.2.7 on 2020-08-06 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tigapublic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stormdrain',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='stormdrainuserversions',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
