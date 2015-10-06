#-*-coding=utf-8-*-

from django.conf.urls.defaults import patterns

urlpatterns = patterns('apps.main',
    #main
    (r'^login.ajax', 'main_views.login'),
    
    #user
    (r'^test', 'main_views.test'),
    
    #finally
	(r'^.*\.html$', 'main_views.default_html'),
	(r'$', 'main_views.default_page'),
)
