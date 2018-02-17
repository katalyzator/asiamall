# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-17 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0008_auto_20180216_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoplike',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_shop_like', to='fcm_django.FCMDevice'),
        ),
        migrations.AlterField(
            model_name='shoplike',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_likes', to='shops.Shop'),
        ),
    ]