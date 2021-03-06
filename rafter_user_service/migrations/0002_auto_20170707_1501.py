# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 20:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rafter_user_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('method', models.CharField(max_length=200)),
                ('protocol', models.FileField(max_length=200, upload_to='')),
                ('consent', models.FileField(max_length=200, upload_to='')),
                ('recruitment', models.FileField(max_length=200, upload_to='')),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvestigationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('affiliation', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Literature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publication_date', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('reference', models.CharField(max_length=200)),
                ('bibtex', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='literature_creator', to='rafter_user_service.Investigator')),
                ('experiment', models.ManyToManyField(to='rafter_user_service.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Manipulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manipulation_creator', to='rafter_user_service.Investigator')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manipulation_last_modifier', to='rafter_user_service.Investigator')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('literature_reference', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_creator', to='rafter_user_service.Investigator')),
                ('input', models.ManyToManyField(to='rafter_user_service.Input')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_last_modifier', to='rafter_user_service.Investigator')),
            ],
        ),
        migrations.CreateModel(
            name='ModelStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelstatus_creator', to='rafter_user_service.Investigator')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelstatus_last_modifier', to='rafter_user_service.Investigator')),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='output_creator', to='rafter_user_service.Investigator')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='output_last_modifier', to='rafter_user_service.Investigator')),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameter_creator', to='rafter_user_service.Investigator')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameter_last_modifier', to='rafter_user_service.Investigator')),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='population_creator', to='rafter_user_service.Investigator')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='population_last_modifier', to='rafter_user_service.Investigator')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectstate_creator', to='rafter_user_service.Investigator')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectstate_last_modifier', to='rafter_user_service.Investigator')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_creator', to='rafter_user_service.Investigator')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_last_modifier', to='rafter_user_service.Investigator')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('affiliation', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('created_by', models.CharField(max_length=200, unique=True)),
                ('modified_by', models.CharField(max_length=200, unique=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theory_creator', to='rafter_user_service.Investigator')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theory_last_modifier', to='rafter_user_service.Investigator')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatment_creator', to='rafter_user_service.Investigator')),
                ('manipulation', models.ManyToManyField(to='rafter_user_service.Manipulation')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatment_last_modifier', to='rafter_user_service.Investigator')),
                ('population', models.ManyToManyField(to='rafter_user_service.Population')),
            ],
        ),
        migrations.AddField(
            model_name='model',
            name='output',
            field=models.ManyToManyField(to='rafter_user_service.Output'),
        ),
        migrations.AddField(
            model_name='model',
            name='parameter',
            field=models.ManyToManyField(to='rafter_user_service.Parameter'),
        ),
        migrations.AddField(
            model_name='model',
            name='theory',
            field=models.ManyToManyField(to='rafter_user_service.Theory'),
        ),
        migrations.AddField(
            model_name='literature',
            name='model',
            field=models.ManyToManyField(to='rafter_user_service.Model'),
        ),
        migrations.AddField(
            model_name='literature',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='literature_last_modifier', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='literature',
            name='theory',
            field=models.ManyToManyField(to='rafter_user_service.Theory'),
        ),
        migrations.AddField(
            model_name='investigator',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rafter_user_service.Team'),
        ),
        migrations.AddField(
            model_name='investigator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investigationstatus',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investigationstatus_creator', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='investigationstatus',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investigationstatus_last_modifier', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='input',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_creator', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='input',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_last_modifier', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='experimentstatus',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experimentstatus_creator', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='experimentstatus',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experimentstatus_last_modifier', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiment_creator', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='manipulation',
            field=models.ManyToManyField(to='rafter_user_service.Manipulation'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiment_last_modifier', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='population',
            field=models.ManyToManyField(to='rafter_user_service.Population'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='treatment',
            field=models.ManyToManyField(to='rafter_user_service.Treatment'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis_creator', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='input',
            field=models.ManyToManyField(to='rafter_user_service.Input'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis_last_modifier', to='rafter_user_service.Investigator'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='output',
            field=models.ManyToManyField(to='rafter_user_service.Output'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='parameter',
            field=models.ManyToManyField(to='rafter_user_service.Parameter'),
        ),
    ]
