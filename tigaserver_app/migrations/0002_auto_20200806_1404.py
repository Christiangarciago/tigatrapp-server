# Generated by Django 2.2.7 on 2020-08-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tigaserver_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='utmX',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='utmY',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]