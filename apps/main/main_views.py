#-*-coding=utf-8-*-

import os
import json

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.template.loader import get_template
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def default_page(request):
    if request.path in ("/", ""):
        return HttpResponseRedirect('/account/content')
    else:
        raise Http404()

def default_html(request):
    template_path = request.path[1:]
    file_path = os.path.join(__file__, "../../" + template_path)
    file_path = os.path.normpath(file_path)

    if os.path.exists(file_path):
        template = get_template(template_path)
        variables = RequestContext(request, {})
        output = template.render(variables)
        return HttpResponse(output, content_type = "text/html; charset=UTF-8")
    else:
        raise Http404()


def login(request):
    user_name = request.POST["username"].encode("utf8")
    user_password = request.POST["password"].encode("utf8")
    next = request.POST.get("next", "/").encode("utf8")
    result_data = {"status": 1, "message": '输入格式不正确',}

    user = authenticate(username=user_name, password=user_password)
    if not user:
        message = "用户“" + user_name + "”不存在，或密码错误"
        result_data = {"status": -1, "message": message}
        return HttpResponse(json.dumps(result_data), content_type='application/json; charset=UTF-8')
    auth_login(request, user)
    result_data = {"status": 0, "message": "登录成功", "next_url": next,}
    return HttpResponse(json.dumps(result_data), content_type='application/json; charset=UTF-8')

def test(request):
    template = get_template('main/template/base.html')
    variables = RequestContext(request,{
        "stock_info_list" : "stock_info_list",
    })
    output = template.render(variables)    
    return HttpResponse(output, content_type = "text/html; charset=UTF-8")

