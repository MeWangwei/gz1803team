from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail
from django.core.cache import cache
from .my_util import get_random_syr
from django.template import loader
from django.core.cache import cache
# Create your views here.

def send_my_email(req):
    title='呵呵'
    msg='传说中的一等奖'
    email_from=settings.DEFAULT_FROM_EMAIL
    reciever = [
        '872898324@qq.com'
    ]
    send_mail(title,msg,email_from,reciever)
    return HttpResponse('OK')


def send_email_v1(req):
    title = "阿里offer"
    msg = " "
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '872898324@qq.com',
    ]
    # 加载模板
    template = loader.get_template('email.html')
    # 渲染模板
    html_str = template.render({'msg': '双击666'})

    # 发送邮件
    send_mail(title, msg, email_from, reciever, html_message=html_str)
    return HttpResponse("ok")

def verify(req):
    if req.method == "GET":
        return render(req,'verify.html')
    else:
        param = req.POST
        email = param.get('email')
        random_str = get_random_syr()
        url = 'http://120.79.245.200:12348/man08/jihuo/'+random_str
        tmp = loader.get_template('active.html')
        html_str = tmp.render({'url':url})
        title = '呵呵'
        msg = ''
        email_from = settings.DEFAULT_FROM_EMAIL
        reciever = [
            email,
        ]
        send_mail(title, msg, email_from, reciever, html_message=html_str)
        cache.set(random_str, email, 200)
        return HttpResponse("ok")

def jihuo(req,str1):
    res = cache.get(str1)
    if res:
        return HttpResponse(res+"激活成功")
    else:
        return HttpResponse("验证连接无效")

def send_many_email(req):
    title = "恭喜你中了一等奖"
    msg = '特奖励澧县1日游'
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever1 = [
        '337609271@qq.com',
        '872898324@qq.com'
    ]
    msg1 = (title, msg, email_from, reciever1)
    msg2 = (title, msg, email_from, ['872898324@qq.com', '337609271@qq.com'])

    send_mass_mail((msg1, msg2), fail_silently=True)
    return HttpResponse("ok")
