# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rafter_user_service', '0023_auto_20170922_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinvestigation',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
