# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin

from main.models import Slider, AboutAsiaMall, Lessee, Advertiser, Application

from modeltranslation.translator import TranslationOptions, translator, register

from main.models import *


class AboutAsiaMallTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


class LesseeAsiaMallTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


class AdvertiserAsiaMallTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


translator.register(Lessee, LesseeAsiaMallTranslationOptions)
translator.register(Advertiser, AdvertiserAsiaMallTranslationOptions)
translator.register(AboutAsiaMall, AboutAsiaMallTranslationOptions)


class AboutAsiaMallAdmin(TabbedExternalJqueryTranslationAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

    class Meta:
        model = AboutAsiaMall


class LesseeAdmin(TabbedExternalJqueryTranslationAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

    class Meta:
        model = Lessee


class AdvertiserAdmin(TabbedExternalJqueryTranslationAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

    class Meta:
        model = Advertiser


admin.site.register(Slider)
admin.site.register(AboutAsiaMall, AboutAsiaMallAdmin)
admin.site.register(Lessee, LesseeAdmin)
admin.site.register(Advertiser, AdvertiserAdmin)
admin.site.register(Application)
