# -*- coding: utf-8 -*-

import datetime
from django.core.context_processors import csrf
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from livesettings import config_value

from pages.models import Page
from order.forms import RequestForm
from news.models import Article
from slideshow.models import Slider
from reviews.models import Review

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c.update(csrf(request))
    
    return c

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['settings'] = { 'money_from': config_value('MyApp', 'SUM_START'),
                      'money_to': config_value('MyApp',   'SUM_END'),
                      'time_from': config_value('MyApp',  'TIME_START'),
                      'time_to': config_value('MyApp',    'TIME_END'),
                      'percent': config_value('MyApp',    'PERCENT')  }
    c['slider'] = Slider.objects.filter(show=True)
    c['news'] = Article.objects.all()
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def other_page(request, page_name):
    c = get_common_context(request)
    try:
        c.update(Page.get_by_slug(page_name))
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()
    
def news_page(request, page_name):
    c = get_common_context(request)
    try:
        c['item'] = Article.get_by_slug(page_name)
        return render_to_response('news_article.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()

def request_page(request):
    c = get_common_context(request)

    if request.POST:
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            form = RequestForm()
            messages.success(request, u'Ваша заявка успешно отправлена.')
    else:
        form = RequestForm()

    c['form'] = form

    return render_to_response('request.html', c, context_instance=RequestContext(request))