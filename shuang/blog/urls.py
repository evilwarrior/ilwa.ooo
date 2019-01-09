#coding:utf8
from django.urls import re_path
from . import views
 
urlpatterns = [
    re_path(r'^post/(?P<id>\d+)/$', views.Detail, name="blog_detail"),
    re_path(r'^category/(?P<cat>\w+)/$', views.search_cat, name="search_cat"),
    re_path(r'^year/(?P<year>\d+)/$', views.search_year, name="search_year"),
    re_path(r'^tag/(?P<tag>[\w\s]+)/$', views.search_tag, name="search_tag"),
    re_path(r'^$', views.home, name="blog_home"),
]

handler404 = views.page_not_found
