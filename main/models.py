# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
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


class AboutAsiaMall(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null=True)
    text = RichTextUploadingField(verbose_name='Контент')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Об Asia Mall'
        verbose_name = 'Объект'

    def __unicode__(self):
        return smart_unicode(self.title)


class Lessee(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null=True)
    text = RichTextUploadingField(verbose_name='Контент')
    phone_number1 = models.CharField(max_length=255, verbose_name='Номер телефона №1', blank=True, null=True)
    phone_number2 = models.CharField(max_length=255, verbose_name='Номер телефона №2', blank=True, null=True)
    email = models.EmailField(verbose_name='Email')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Арендаторам'
        verbose_name = 'Объект'

    def __unicode__(self):
        return smart_unicode(self.title)


class Advertiser(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null=True)
    text = RichTextUploadingField(verbose_name='Контент')
    phone_number1 = models.CharField(max_length=255, verbose_name='Номер телефона №1', blank=True, null=True)
    phone_number2 = models.CharField(max_length=255, verbose_name='Номер телефона №2', blank=True, null=True)
    email = models.EmailField(verbose_name='Email')
    commercial_file = models.FileField(upload_to='commercial/files', verbose_name='Коммерческое предложение',
                                       blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Рекламодателям'
        verbose_name = 'Объект'

    def __unicode__(self):
        return smart_unicode(self.title)


class Application(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    square = models.CharField(max_length=255, verbose_name='Площадь')
    type_of_product = models.CharField(max_length=255, verbose_name='Тип товара')
    brand = models.CharField(max_length=255, verbose_name='Бренд')

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'Заявки на аренду'

    def __unicode__(self):
        return smart_unicode(self.full_name)
