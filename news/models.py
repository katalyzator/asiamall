# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.encoding import smart_unicode
from fcm_django.models import FCMDevice


def clean_html(raw_html):
    clean_r = re.compile('<.*?>')
    clean_text = re.sub(clean_r, '', raw_html)
    return clean_text[0:100]


class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Тэги'
        verbose_name = 'Тэг'

    def __unicode__(self):
        return smart_unicode(self.title)


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    image = models.ImageField(upload_to='news/images', verbose_name='Главная картинка новости', blank=True, null=True)
    video = models.FileField(verbose_name='Видео', blank=True, null=True)
    tag = models.ForeignKey(Tag, blank=True, null=True, verbose_name='Tags')
    text = RichTextUploadingField(verbose_name='Контент новости')
    share_url = models.CharField(max_length=1000, verbose_name='Ссылка для кнопки поделиться', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Раздел новостей'
        verbose_name = 'Новость'
        ordering = ['-timestamp']

    def __unicode__(self):
        return smart_unicode(self.title)

    def save(self, *args, **kwargs):
        devices = FCMDevice.objects.all()
        devices.send_message(title=self.title, body=self.title, icon="http://149.202.123.241" + self.image.url,
                             sound="default",
                             content_available=True,
                             data={"type": "news", "image": "http://149.202.123.241" + self.image.url},
                             click_action="news")
        super(News, self).save(*args, **kwargs)
