# coding=utf-8
# coding=utf-8
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^add/$', views.add),
    re_path(r'^edit/$', views.edit),
    re_path(r'^delete/$', views.delete)
]
