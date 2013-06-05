# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
import pytils

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name=u'название')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'подкатегория в ->')
    order = models.IntegerField(default=0, verbose_name=u'порядок')
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __unicode__(self):
        return '%s%s' % (' -- ' * self.level, self.name)
    
    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = u'категории'


class Employee(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'категория')
    name = models.CharField(max_length=256, verbose_name=u'ФИО')
    position = models.CharField(max_length=256, blank=True, verbose_name=u'должность')
    text = RichTextField(verbose_name=u'описание', blank=True)
    photo = models.FileField(upload_to= 'uploads/employee', blank=True, max_length=256, verbose_name=u'фото')
   
    class Meta:
        verbose_name = u'работник'
        verbose_name_plural = u'работники'
        ordering = ['name']
    
    def __unicode__(self):
        return self.name