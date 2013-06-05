# -*- coding: utf-8 -*-
from django.db import models

class Slider(models.Model):
    image = models.FileField(upload_to= 'uploads/slider', max_length=256, verbose_name=u'картинка', help_text=u'Размер 996x523')
    content= models.TextField(verbose_name=u'html-описание')
    show = models.BooleanField(default=True, verbose_name=u'показывать на сайте?', help_text=u'Отметьте галочкой, чтобы показывать этот слайд')
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'порядок сортировки', help_text=u'№ слайдера: 1й, 2й или 3й')
    
    class Meta:
        verbose_name = 'слайдер'
        verbose_name_plural = 'слайдер'
        ordering = ['sort_parameter']
    
    