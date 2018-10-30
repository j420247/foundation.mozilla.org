# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-29 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0013_auto_20181023_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='booleanvote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rangevote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]