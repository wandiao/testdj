# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import inspect

from django.contrib import admin

import models as app_models
# Register your models here.
for attr in dir(app_models):
    model = getattr(app_models, attr)
    if not inspect.isclass(model):
        continue

    try:
        admin.site.register(model)
    except:
        pass
