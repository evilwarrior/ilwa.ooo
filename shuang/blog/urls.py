#coding:utf8
from django.conf.urls import url
from . import views
 
urlpatterns = [
    url('test/', views.Test, name="blog_test"),
]
