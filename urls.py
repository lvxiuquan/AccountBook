#-*-coding=utf-8-*-
import os
from django.conf.urls.defaults import patterns, include, url
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import admin
admin.autodiscover()

import inspect

urlpatterns = patterns('',
    # 对login中的资源，特别处理。文档：https://docs.djangoproject.com/en/dev/topics/auth/ 这个要在apache静态资源映射前面
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'main/template/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
                       
    # 对admin中的资源，特别处理      
    url(r'^accounts/admin/', include(admin.site.urls)),
    (r'^static/admin/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': os.path.normpath(os.path.join(inspect.getfile(admin), "../static/admin")),
        'show_indexes': False
    }),
    
    # 静态资源目录，特别处理。如果放在Apache中，自有Apache的映射规则进行操作。
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': os.path.normpath(os.path.join(__file__, "../static")),
        'show_indexes': False
    }),
                       
    url(r'^account/', include('apps.account.account_urls')),
    
    (r'^', include('apps.main.main_urls')),
)