# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from shops.models import Shop, Category, ShopLike


class ShopAdmin(admin.ModelAdmin):
    class Meta:
        model = Shop

    list_display = ['title', 'like_counts']


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category)
admin.site.register(ShopLike)
