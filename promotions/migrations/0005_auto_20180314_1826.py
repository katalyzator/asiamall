# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-14 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0004_auto_20180312_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Tag', verbose_name='Tags'),
        ),
    ]
