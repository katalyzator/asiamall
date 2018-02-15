# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fcm_django', '0003_auto_20170313_1314'),
        ('main', '0005_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=1000, verbose_name='Device_id')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('fcm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcm_django.FCMDevice', verbose_name='FCM Device')),
            ],
            options={
                'verbose_name': 'device_id',
                'verbose_name_plural': 'Devices',
            },
        ),
        migrations.AddField(
            model_name='application',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
