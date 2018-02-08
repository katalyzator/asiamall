# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.encoding import smart_unicode


class Promotion(models.Model):
    PROMOTION_TAG = (
        ('Актульно', 'Актульно'),
        ('Горячее', 'Горячее'),
        ('Оповещение', 'Оповещение')
    )

    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    image = models.ImageField(upload_to='promotions/images', verbose_name='Главная картинка акции', blank=True,
                              null=True)
    tag = models.CharField(max_length=255, verbose_name='Тэг', choices=PROMOTION_TAG)
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')

    text = RichTextUploadingField(verbose_name='Контент акции')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Раздел акий'
        verbose_name = 'акцию'

    def __unicode__(self):
        return smart_unicode(self.title)
