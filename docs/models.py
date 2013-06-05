# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name=u'название')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'является подкатегорией в ->')
    order = models.IntegerField(default=0, blank=True, verbose_name=u'порядок')
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __unicode__(self):
        return '%s%s' % (' -- ' * self.level, self.name)
    
    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = u'категории'


class DocFile(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'категория')
    name = models.CharField(max_length=128, verbose_name=u'название')
    date = models.DateField(auto_now=True, verbose_name=u'дата')
    desc = models.CharField(max_length=512, blank=True, verbose_name=u'описание')
    file = models.FileField(upload_to= 'uploads/docs', blank=True, max_length=256, verbose_name=u'файл', help_text=u'')
    order = models.IntegerField(default=0, blank=True, verbose_name=u'порядок')
    
    class Meta:
        verbose_name = u'файл'
        verbose_name_plural = u'файлы'
        ordering = ['order']
    
    def __unicode__(self):
        return self.name
