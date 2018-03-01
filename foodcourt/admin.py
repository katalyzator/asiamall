# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin

from foodcourt.models import FoodCourt, FoodCourtLike


class FoodCourtAdmin(TabbedExternalJqueryTranslationAdmin):
    class Meta:
        model = FoodCourt

    list_display = ['title', 'like_counts']


admin.site.register(FoodCourt, FoodCourtAdmin)
admin.site.register(FoodCourtLike)
