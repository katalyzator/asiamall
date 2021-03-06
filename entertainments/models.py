# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models

from django.utils.encoding import smart_unicode
from fcm_django.models import FCMDevice


class Entertainment(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Описание"))
    full_description = models.TextField(verbose_name=_("Полное информация"))
    time_start = models.TimeField(blank=True, null=True, verbose_name=_("Время начало работы"))
    time_end = models.TimeField(blank=True, null=True, verbose_name=_("Время окончание работы"))
    image = models.ImageField(upload_to='images/shops', verbose_name=_("Картинка"))
    phone_number = models.CharField(max_length=255, verbose_name=_("Номер телефона"))
    like_counts = models.IntegerField(verbose_name='Количество лайкой', blank=True, null=True, editable=False,
                                      default=0)

    logo = models.ImageField(upload_to='entertainments/logos', verbose_name='Логотип объекта', blank=True, null=True)
    facebook = models.CharField(max_length=255, verbose_name='facebook', blank=True, null=True)
    share_url = models.CharField(max_length=255, verbose_name='Ссылка для кнопки поделиться', blank=True, null=True)
    instagram = models.CharField(max_length=255, verbose_name='Instagram', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = _('Развлечения')
        verbose_name = _('объект')

    def __unicode__(self):
        return smart_unicode(self.title)


class EntertainmentLike(models.Model):
    LIKE_VALUE = (
        (1, 1),
        (-1, -1)
    )
    shop = models.ForeignKey(Entertainment, related_name='entertainment_likes')
    device = models.ForeignKey(FCMDevice, related_name='device_entertainment_like')

    value = models.IntegerField(choices=LIKE_VALUE, verbose_name='Значение голоса')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Рейтинг entertainment'
        verbose_name = 'Объект'

    def __unicode__(self):
        return smart_unicode(self.device)
