# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rafter_user_service', '0002_auto_20170707_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='_token',
            field=models.TextField(max_length=200, null=True),
        ),
    ]