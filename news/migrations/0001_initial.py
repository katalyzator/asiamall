# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 09:56
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('image', models.ImageField(upload_to='news/images', verbose_name='\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u043d\u043e\u0432\u043e\u0441\u0442\u0438')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442 \u043d\u043e\u0432\u043e\u0441\u0442\u0438')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439',
            },
        ),
    ]