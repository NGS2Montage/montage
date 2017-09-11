# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-22 16:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('montage_jwt', '0002_auto_20170818_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='jwt',
            name='exp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jwt',
            name='scope',
            field=models.CharField(editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='jwt',
            name='token',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='jwt',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
