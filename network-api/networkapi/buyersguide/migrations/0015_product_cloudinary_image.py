# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 10:34
from __future__ import unicode_literals

from django.db import migrations
import networkapi.buyersguide.models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0014_auto_20181029_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cloudinary_image',
            field=networkapi.buyersguide.models.CloudinaryImageField(blank=True, help_text='Image representing this product', max_length=255),
        ),
    ]
