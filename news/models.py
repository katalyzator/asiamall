# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urlparse

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.encoding import smart_unicode


class News(models.Model):
    NEWS_TAG = (
        ('Актульно', 'Актульно'),
        ('Горячее', 'Горячее'),
        ('Оповещение', 'Оповещение')
    )

    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    image = models.ImageField(upload_to='news/images', verbose_name='Главная картинка новости', blank=True, null=True)
    video = models.FileField(verbose_name='Видео', blank=True, null=True)
    tag = models.CharField(max_length=255, verbose_name='Тэг', choices=NEWS_TAG)

    text = RichTextUploadingField(verbose_name='Контент новости')
    share_url = models.CharField(max_length=1000, verbose_name='Ссылка для кнопки поделиться', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Раздел новостей'
        verbose_name = 'Новость'

    def __unicode__(self):
        return smart_unicode(self.title)
