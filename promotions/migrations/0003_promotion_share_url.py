# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_promotion_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='share_url',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f'),
        ),
    ]
