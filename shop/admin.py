# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from shop.models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)