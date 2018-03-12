# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin

from shops.models import Shop, Category, ShopLike

from modeltranslation.translator import TranslationOptions, translator

from shops.models import Category


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Category, CategoryTranslationOptions)


class CategoryAdmin(TabbedExternalJqueryTranslationAdmin):
    class Meta:
        model = Category


class ShopAdmin(TabbedExternalJqueryTranslationAdmin):
    class Meta:
        model = Shop

    list_display = ['id', 'title', 'like_counts']


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ShopLike)
