# -*- coding: utf-8 -*-
from django.contrib import admin
import models
from mptt.admin import MPTTModelAdmin


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name', )
    mptt_level_indent = 20

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'position')
    search_fields = ('name', 'text')
    ordering = ('name', )

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Employee, EmployeeAdmin)
