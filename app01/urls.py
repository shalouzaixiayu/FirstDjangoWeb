# -*- coding :  utf-8 -*-
# @Time      :  2020/12/10  16:26
# @author    :  沙漏在下雨
# @Software  :  PyCharm
# @CSDN      :  https://me.csdn.net/qq_45906219
from django.urls import path
from app01 import views

app_name = "index"

urlpatterns = [
    path('index.html', views.index, name="index"),
]
