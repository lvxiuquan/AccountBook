#-*-coding=utf-8-*-

import json
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from libs.facility.decorators import check_login
from account_api import AccountApi

def account_list(request):
    user_dic = {
        "lv": "吕修权",
        "yu": "余涛涛",
        "xu": "徐文琪",
        "dong": "虞冬",
    }
    account_handler = AccountApi(request.user)
    presents = account_handler.get_present()
    account_info_list = account_handler.get_accounts()
    template = get_template('account/template/account_list.html')
    variables = RequestContext(request,{
        "Account" : user_dic,
        "account_list": account_info_list,
        "presents": presents,
    })
    output = template.render(variables)
    return HttpResponse(output, content_type = "text/html; charset=UTF-8")

@check_login()
def submit_account_ajax(request):
    push_data = json.loads(request.POST.get("push_data"))
    account_handler = AccountApi(request.user)
    response_data = account_handler.keep_account(push_data)
    return HttpResponse(json.dumps(response_data), content_type = "text/html; charset=UTF-8")