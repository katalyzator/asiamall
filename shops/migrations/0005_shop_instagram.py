# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_shop_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='instagram',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Instagram'),
        ),
    ]