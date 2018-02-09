# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438')),
                ('image', models.ImageField(upload_to='slider/images', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0443',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440',
            },
        ),
    ]
