# Generated by Django 2.2.7 on 2020-09-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tigaserver_app', '0002_auto_20200807_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='note',
            field=models.TextField(blank=True, help_text='Note user attached to report.', null=True),
        ),
    ]
