#coding:utf8
from django.contrib import admin
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
         
admin.site.register(Article,ArticleAdmin)
