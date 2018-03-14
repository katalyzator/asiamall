# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin

from news.models import News, Tag

from modeltranslation.translator import TranslationOptions, translator


class TagTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Tag, TagTranslationOptions)


class TagAdmin(TabbedExternalJqueryTranslationAdmin):
    class Meta:
        model = Tag


admin.site.register(News)
admin.site.register(Tag, TagAdmin)
