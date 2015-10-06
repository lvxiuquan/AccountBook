#-*-coding=utf-8-*-

from django.conf.urls.defaults import patterns

urlpatterns = patterns('apps.account',
    (r'^content', 'account_views.account_list'),
    (r'^submit_account.ajax', 'account_views.submit_account_ajax'),
    
)
