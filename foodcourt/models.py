# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext as _
from django.db import models
from fcm_django.models import FCMDevice


class FoodCourt(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Описание"))
    full_description = models.TextField(verbose_name=_("Полное информация"))
    time_start = models.TimeField(blank=True, null=True, verbose_name=_("Время начало работы"))
    time_end = models.TimeField(blank=True, null=True, verbose_name=_("Время окончание работы"))
    image = models.ImageField(upload_to='images/shops', verbose_name=_("Картинка"))
    phone_number = models.CharField(max_length=255, verbose_name=_("Номер телефона"))
    logo = models.ImageField(upload_to='food_court/logos', verbose_name='Логотип объекта', blank=True, null=True)
    like_counts = models.IntegerField(verbose_name='Количество лайкой', blank=True, null=True, editable=False,
                                      default=0)
    facebook = models.CharField(max_length=255, verbose_name='facebook', blank=True, null=True)
    share_url = models.CharField(max_length=255, verbose_name='Ссылка для кнопки поделиться', blank=True, null=True)
    instagram = models.CharField(max_length=255, verbose_name='Instagram', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = _('Фудкорт')
        verbose_name = _('объект')

    def __unicode__(self):
        return smart_unicode(self.title)


class FoodCourtLike(models.Model):
    LIKE_VALUE = (
        (1, 1),
        (-1, -1)
    )
    shop = models.ForeignKey(FoodCourt, related_name='foodcourt_likes')
    device = models.ForeignKey(FCMDevice, related_name='device_foodcourt_like')

    value = models.IntegerField(choices=LIKE_VALUE, verbose_name='Значение голоса')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Рейтинг FoodCourt'
        verbose_name = 'Объект'

    def __unicode__(self):
        return smart_unicode(self.device)
