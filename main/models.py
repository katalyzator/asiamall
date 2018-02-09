# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import smart_unicode


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок картинки')
    image = models.ImageField(upload_to='slider/images', verbose_name='Картинка')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Слайдер'
        verbose_name = 'Картинку'

    def __unicode__(self):
        return smart_unicode(self.title)
