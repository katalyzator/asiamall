# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-12 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20180222_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0422\u044d\u0433',
                'verbose_name_plural': '\u0422\u044d\u0433\u0438',
            },
        ),
        migrations.AlterField(
            model_name='news',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Tag', verbose_name='\u0422\u0438\u043f \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
    ]
