# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from foodcourt.models import FoodCourt, FoodCourtLike

admin.site.register(FoodCourt)
admin.site.register(FoodCourtLike)
