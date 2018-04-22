# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-22 17:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u79d1\u6280\u6210\u679c\u4fe1\u606f')),
                ('image', models.ImageField(upload_to='banner/%y/%m', verbose_name='\u56fe\u7247')),
                ('type', models.CharField(max_length=50, verbose_name='\u7c7b\u578b')),
                ('subject', models.CharField(max_length=50, verbose_name='\u6240\u5c5e\u5b66\u79d1')),
                ('number', models.CharField(max_length=50, verbose_name='\u7f16\u53f7')),
                ('price', models.IntegerField(default=0, verbose_name='\u4ef7\u683c')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u5546\u54c1\u4fe1\u606f',
            },
        ),
    ]