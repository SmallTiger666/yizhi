# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-21 10:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPLat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutplat', models.TextField(verbose_name='\u95dc\u65bc\u5e73\u81fa')),
                ('image', models.ImageField(upload_to='banner/%y/%m', verbose_name='\u5716\u7247')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u6642\u9593')),
            ],
            options={
                'verbose_name': '\u95dc\u65bc\u5e73\u81fa',
                'verbose_name_plural': '\u95dc\u65bc\u5e73\u81fa',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6a19\u984c')),
                ('image', models.ImageField(upload_to='banner/%y/%m', verbose_name='\u8f2a\u64ad\u5716')),
                ('url', models.URLField(verbose_name='\u8a2a\u554f\u5730\u5740')),
                ('index', models.IntegerField(default=100, verbose_name='\u9806\u5e8f')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u6642\u9593')),
            ],
            options={
                'verbose_name': '\u8f2a\u64ad\u5716',
                'verbose_name_plural': '\u8f2a\u64ad\u5716',
            },
        ),
        migrations.CreateModel(
            name='MainTechnology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
