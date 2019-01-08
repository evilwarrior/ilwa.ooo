#coding:utf8
from django.urls import re_path
from . import views
 
urlpatterns = [
    re_path(r'^post/(?P<id>\d+)/$', views.Detail, name="blog_detail"),
    re_path(r'^$', views.home, name="blog_home"),
]

handler404 = views.page_not_found
