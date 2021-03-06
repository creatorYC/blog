# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content_md', models.TextField()),
                ('content_html', models.TextField()),
                ('read_count', models.IntegerField()),
                ('summary', models.CharField(max_length=300)),
                ('tags', models.CharField(max_length=30)),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
                ('deleted', models.BooleanField()),
                ('allow_comment', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('psw', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('image', models.CharField(max_length=100)),
                ('gender', models.BooleanField()),
                ('status', models.BooleanField()),
                ('validate_code', models.CharField(max_length=50)),
                ('register_time', models.DateTimeField()),
            ],
        ),
    ]
