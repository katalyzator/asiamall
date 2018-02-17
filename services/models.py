# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext as _
from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Описание"))
    full_description = models.TextField(verbose_name=_("Полное информация"))
    time_start = models.TimeField(blank=True, null=True, verbose_name=_("Время начало работы"))
    time_end = models.TimeField(blank=True, null=True, verbose_name=_("Время окончание работы"))
    image = models.ImageField(upload_to='images/shops', verbose_name=_("Картинка"))
    phone_number = models.CharField(max_length=255, verbose_name=_("Номер телефона"))
    logo = models.ImageField(upload_to='food_court/logos', verbose_name='Логотип объекта', blank=True, null=True)
    facebook = models.CharField(max_length=255, verbose_name='facebook', blank=True, null=True)
    share_url = models.CharField(max_length=255, verbose_name='Ссылка для кнопки поделиться', blank=True, null=True)
    instagram = models.CharField(max_length=255, verbose_name='Instagram', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = _('Услуги')
        verbose_name = _('объект')

    def __unicode__(self):
        return smart_unicode(self.title)