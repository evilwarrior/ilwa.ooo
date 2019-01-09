#coding:utf8
from django.contrib import admin
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    def save_model(self, request, obj, form, change):
        if str(obj.authors) == '':
            obj.authors = str(request.user)
        if str(obj.category) == '':
            obj.category = '日记'
        super().save_model(request, obj, form, change)

admin.site.register(Article, ArticleAdmin)
