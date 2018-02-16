# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from shops.models import Shop, Category, ShopLike

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(ShopLike)