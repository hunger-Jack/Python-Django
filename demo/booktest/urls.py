"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path
from booktest import views


urlpatterns = [
    re_path(r"^index2$", views.index, name="index"),  # 无参数反向解析
    re_path(r"^index2/(\d+)$", views.index, name="index"),  # 有位置参数的反向解析
    re_path(r"^index2/(?P<num>\d+)$", views.index, name="index"),  # 有关键字参数的反向解析
    re_path(r"^index$", views.index),
    re_path(r"^books$", views.show_books),
    re_path(r"^books/(\d+)$", views.show_heros),
    re_path(r"^create$", views.create),
    re_path(r"^delete(\d+)$", views.delete),
    re_path(r"^areas$", views.areas),
    re_path(r"^login_form$", views.login_form),
    re_path(r"^login_form_check$", views.login_form_check),
    re_path(r"^login_ajax$", views.login_ajax),
    re_path(r"^login_ajax_check$", views.login_ajax_check),
    re_path(r"^change_pwd$", views.change_pwd),
    re_path(r"^change_pwd_action$", views.change_pwd_action),
    re_path(r"^verify_code$", views.verify_code),
]
