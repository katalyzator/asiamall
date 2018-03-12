# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.encoding import smart_unicode
from fcm_django.models import FCMDevice


class Promotion(models.Model):
    PROMOTION_TAG = (
        (u'Актуально', u'Актуально'),
        (u'Горячее', u'Горячее'),
        (u'Оповещение', u'Оповещение')
    )

    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    image = models.ImageField(upload_to='promotions/images', verbose_name='Главная картинка акции', blank=True,
                              null=True)
    tag = models.CharField(max_length=255, verbose_name='Тэг', choices=PROMOTION_TAG, blank=True, null=True)
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    share_url = models.CharField(max_length=1000, verbose_name='Ссылка для кнопки поделиться', blank=True, null=True)

    text = RichTextUploadingField(verbose_name='Контент акции')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Раздел акий'
        verbose_name = 'акцию'

    def __unicode__(self):
        return smart_unicode(self.title)

    def save(self, *args, **kwargs):
        devices = FCMDevice.objects.all()
        devices.send_message(title=self.title, body=self.title,
                             icon="http://149.202.123.241" + self.image.url,
                             sound="default",
                             content_available=True,
                             data={"type": "promotion", "image": "http://149.202.123.241" + self.image.url},
                             click_action="promotion")

        super(Promotion, self).save(*args, **kwargs)
