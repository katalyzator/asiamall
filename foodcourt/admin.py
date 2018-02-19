# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from foodcourt.models import FoodCourt, FoodCourtLike


class FoodCourtAdmin(admin.ModelAdmin):
    class Meta:
        model = FoodCourt

    list_display = ['title', 'like_counts']


admin.site.register(FoodCourt, FoodCourtAdmin)
admin.site.register(FoodCourtLike)
