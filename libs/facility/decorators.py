#-*-coding=utf-8-*-
'''框架的函数修饰符
'''
import urlparse
from django.contrib.auth.decorators import login_required, permission_required

def check_login(login_url = '/accounts/login/', message = '本操作需要登入', suppress_alert = False):
    new_login_url = add_alert_to_url(login_url, message, suppress_alert)
    return login_required(login_url = new_login_url)

def add_alert_to_url(login_url, message, suppress_alert):
    ''' 由 <script type="text/javascript" src="/main/static/default.js"></script> 这里面，检查_alerts选项 '''
    suppress_alert_flag = "1" if suppress_alert == True else "0"
    if login_url == None:
        raise ValueError, "login_url cannot be null"
    if message != None:
        scheme, netloc, path, params, query, fragment = urlparse.urlparse(login_url)
        if query == None:
            query = "_alerts=%s&_suppress=%s" % (message, suppress_alert_flag)
        else:
            query = query + "&_alerts=%s&_suppress=%s" % (message, suppress_alert_flag)
        login_url = urlparse.urlunparse((scheme, netloc, path, params, query, fragment))
    return login_url

def check_permission(perm_name, login_url="/main/template/index.html", message = None):
    new_login_url = add_alert_to_url(login_url, message, False)
    return permission_required(perm_name, login_url = new_login_url)
