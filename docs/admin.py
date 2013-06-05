# -*- coding: utf-8 -*-
from django.contrib import admin
import models
from django.db import models as django_models
from django.forms import CheckboxSelectMultiple
from mptt.admin import MPTTModelAdmin

class FileInline(admin.TabularInline): 
    model = models.DocFile
    extra = 3

class CategoryAdmin(MPTTModelAdmin):
    inlines = [FileInline, ]
    list_display = ('name', 'order')
    search_fields = ('name', )
    mptt_level_indent = 20

class FileAdmin(admin.ModelAdmin):
    model = models.DocFile
    list_display = ('name', 'category', 'desc')
    search_fields = ('name', 'desc')
    

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.DocFile, FileAdmin)
