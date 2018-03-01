# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-01 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SvtPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_service', models.CharField(max_length=4)),
                ('month_of_service', models.CharField(max_length=2)),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.AlterField(
            model_name='svtunit',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]
