# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rafter_user_service', '0005_merge_20170828_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysis',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='analysisinstance',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='confirmatoryloop',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='experimentinstance',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='experimentstatus',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='exploratoryloop',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='input',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='investigation',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='investigationstatus',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='literature',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='manipulation',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='model',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='modelinstance',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='modelstatus',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='output',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='parameter',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='population',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='project',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='projectstate',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='role',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='theory',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='theoryinstance',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='rid',
        ),
    ]
