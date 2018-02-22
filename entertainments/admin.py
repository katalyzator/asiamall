# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from entertainments.models import Entertainment, EntertainmentLike


class EntertainmentAdmin(admin.ModelAdmin):
    class Meta:
        model = Entertainment

    list_display = ['title', 'like_counts']


admin.site.register(Entertainment, EntertainmentAdmin)
admin.site.register(EntertainmentLike)
