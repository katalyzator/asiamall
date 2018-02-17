# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import Slider, AboutAsiaMall, Lessee, Advertiser, Application


class AboutAsiaMallAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


class LesseeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


class AdvertiserAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


admin.site.register(Slider)
admin.site.register(AboutAsiaMall, AboutAsiaMallAdmin)
admin.site.register(Lessee, LesseeAdmin)
admin.site.register(Advertiser, AdvertiserAdmin)
admin.site.register(Application)