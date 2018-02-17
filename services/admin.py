# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from services.models import Service, ServiceLike

admin.site.register(Service)
admin.site.register(ServiceLike)
