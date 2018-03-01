# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin

from services.models import Service, ServiceLike


class ServiceAdmin(TabbedExternalJqueryTranslationAdmin):
    class Meta:
        model = Service

    list_display = ['title', 'like_counts']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceLike)
