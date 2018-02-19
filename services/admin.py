# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from services.models import Service, ServiceLike


class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Service

    list_display = ['title', 'like_counts']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceLike)
