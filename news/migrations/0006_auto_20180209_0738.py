# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180208_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='video_img',
        ),
        migrations.AlterField(
            model_name='news',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=b'', verbose_name='\u0412\u0438\u0434\u0435\u043e'),
        ),
    ]
