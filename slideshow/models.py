# -*- coding: utf-8 -*-
from django.db import models

class Slider(models.Model):
    image = models.FileField(upload_to= 'uploads/slider', max_length=256, verbose_name=u'картинка', help_text=u'Размер 996x523')
    title = models.CharField(max_length=256, verbose_name=u'заголовок', help_text=u'В макете это Светлана')
    description = models.CharField(max_length=1024, verbose_name=u'текст', help_text=u'Отзыв Светланы')
    link = models.CharField(max_length=256, blank=True, verbose_name=u'Ссылка', help_text=u'Ссылка снизу, если есть')
    show = models.BooleanField(default=True, verbose_name=u'показывать на сайте?', help_text=u'Отметьте галочкой, чтобы показывать этот слайд')
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'порядок сортировки', help_text=u'№ слайдера: 1й, 2й или 3й')
    
    class Meta:
        verbose_name = 'слайдер'
        verbose_name_plural = 'слайдер'
        ordering = ['sort_parameter']
        
    
    def __unicode__(self):
        return self.title