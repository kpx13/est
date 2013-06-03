# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'sort_parameter')
    ordering = ('sort_parameter', )
    
admin.site.register(models.Review, ReviewAdmin)