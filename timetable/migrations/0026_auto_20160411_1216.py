# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-11 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0025_auto_20160410_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.CharField(default=b'', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='hopkinscourse',
            name='department',
            field=models.CharField(default=b'', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ottawacourse',
            name='department',
            field=models.CharField(default=b'', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='rutgerscourse',
            name='department',
            field=models.CharField(default=b'', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='umdcourse',
            name='department',
            field=models.CharField(default=b'', max_length=250, null=True),
        ),
    ]