# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-12 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180212_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertiser',
            name='commercial_file',
            field=models.FileField(blank=True, null=True, upload_to='commercial/files', verbose_name='\u041a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u043e\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
    ]
