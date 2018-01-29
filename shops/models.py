# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext as _

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название категории"))

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = _("Категории")
        verbose_name = _("Категорию")

    def __unicode__(self):
        return smart_unicode(self.title)


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Разделы'
        verbose_name = 'Раздел'

    def __unicode__(self):
        return smart_unicode(self.title)


class Shop(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Описание"))
    full_description = models.TextField(verbose_name=_("Полное информация"))
    time_start = models.TimeField(blank=True, null=True, verbose_name=_("Время начало работы"))
    time_end = models.TimeField(blank=True, null=True, verbose_name=_("Время окончание работы"))
    image = models.ImageField(upload_to='images/shops', verbose_name=_("Картинка"))
    category = models.ForeignKey(Category, verbose_name=_("Выберите категорию"), related_name='shop_category',
                                 blank=True, null=True)
    service_for = models.ManyToManyField(Service, verbose_name=_("Выберите аудиторию"), related_name='shop_service',
                                         blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = _('Магазины')
        verbose_name = _('Магазин')

    def __unicode__(self):
        return smart_unicode(self.title)
