# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 18:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=80)),
                ('desc', models.TextField(blank=True, max_length=200)),
                ('access_token', models.BinaryField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_roles', models.TextField(default='[]', max_length=200)),
                ('_access', models.TextField(default='["@core", "#public"]', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rafter_user_service.Profile'),
        ),
    ]