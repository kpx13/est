# -*- coding: utf-8 -*-
from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=256, verbose_name=u'имя')
    text = models.CharField(max_length=1024, verbose_name=u'текст отзыва')
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'порядок сортировки', help_text=u'порядковый номер')
    
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ['sort_parameter']
        
    
    def __unicode__(self):
        return self.name