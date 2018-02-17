# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-17 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fcm_django', '0003_auto_20170313_1314'),
        ('entertainments', '0003_entertainment_instagram'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntertainmentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, 1), (-1, -1)], verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0433\u043e\u043b\u043e\u0441\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_entertainment_like', to='fcm_django.FCMDevice')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u044a\u0435\u043a\u0442',
                'verbose_name_plural': '\u0420\u0435\u0439\u0442\u0438\u043d\u0433 entertainment',
            },
        ),
        migrations.AddField(
            model_name='entertainment',
            name='like_counts',
            field=models.IntegerField(blank=True, editable=False, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043b\u0430\u0439\u043a\u043e\u0439'),
        ),
        migrations.AddField(
            model_name='entertainmentlike',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entertainment_likes', to='entertainments.Entertainment'),
        ),
    ]
