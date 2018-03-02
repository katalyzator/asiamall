# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin

from shops.models import Shop, Category, ShopLike


class ShopAdmin(TabbedExternalJqueryTranslationAdmin):
    class Meta:
        model = Shop

    list_display = ['id', 'title', 'like_counts']


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category)
admin.site.register(ShopLike)
