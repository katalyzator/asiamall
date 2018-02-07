# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from entertainments.models import Entertainment

admin.site.register(Entertainment)