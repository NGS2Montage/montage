# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rafter_user_service', '0021_investigation_models'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='input',
            new_name='inputs',
        ),
        migrations.RenameField(
            model_name='model',
            old_name='output',
            new_name='outputs',
        ),
        migrations.RenameField(
            model_name='model',
            old_name='parameter',
            new_name='parameters',
        ),
    ]
