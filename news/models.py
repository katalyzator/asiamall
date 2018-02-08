# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urlparse

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.encoding import smart_unicode


class News(models.Model):

    NEWS_TAG = (
        ('actual', 'Актульно'),
        ('hot', 'Горячее'),
        ('notify', 'Оповещение')
    )

    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    image = models.ImageField(upload_to='news/images', verbose_name='Главная картинка новости', blank=True, null=True)
    video = models.CharField(max_length=1000, verbose_name='Видео ссылка с YouTube', blank=True, null=True)
    video_img = models.CharField(max_length=1000, editable=False, verbose_name='thumbnail')
    tag = models.CharField(max_length=255, verbose_name='Тэг', choices=NEWS_TAG)

    text = RichTextUploadingField(verbose_name='Контент новости')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Раздел новостей'
        verbose_name = 'Новость'

    def __unicode__(self):
        return smart_unicode(self.title)

    def save(self, *args, **kwargs):
        if self.video:
            url_data = urlparse.urlparse(self.video)
            query = urlparse.parse_qs(url_data.query)
            video = query["v"][0]
            self.video_img = 'https://img.youtube.com/vi/' + video + '/0.jpg'
            print self.video_img
        super(News, self).save(*args, **kwargs)
