# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
admin.autodiscover()

import settings
import views

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
    
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^settings/', include('livesettings.urls')),

    url(r'^$' , views.home_page),
    url(r'^news/$' , views.news_page),
    url(r'^news/(?P<page_name>[\w-]+)/$' , views.news_article_page),
    url(r'^docs/$' , views.docs_page),
    url(r'^docs/(?P<id>[\w-]+)/$' , views.docs_page),
    url(r'^team/$' , views.team_page),
    url(r'^team/(?P<id>[\w-]+)/$' , views.team_page),
    url(r'^company/(?P<page_name>[\w-]+)/$' , views.company_page),
    url(r'^(?P<page_name>[\w-]+)/$' , views.other_page),
    
    
)
