# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.encoding import smart_unicode


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    image = models.ImageField(upload_to='news/images', verbose_name='Главная картинка новости', blank=True, null=True)
    video = models.CharField(max_length=1000, verbose_name='Видео ссылка с YouTube', blank=True, null=True)
    video_img = models.CharField(max_length=1000, editable=False, verbose_name='thumbnail')

    text = RichTextUploadingField(verbose_name='Контент новости')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Раздел новостей'
        verbose_name = 'Новость'

    def __unicode__(self):
        return smart_unicode(self.title)
