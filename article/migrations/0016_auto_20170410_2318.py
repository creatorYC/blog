# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20170408_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_desc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_desc',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
