from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^email$',send_my_email),
    url(r'^email_v1$',send_email_v1),
    url(r'^verify$',verify),
    url(r'^jihuo/(.+)',jihuo),
    url(r'^send_many_email$',send_many_email)
]