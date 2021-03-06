#coding:utf8
from django.contrib import admin
from django.conf import settings
# 我的模型类
from blog.models import Article
from blog.models import Criticism

# python其他模块
import os

class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'authors', 'category', 'tags', 'content', 'user_now', )
    list_display = ('title', 'authors', 'pub_date')
    readonly_fields = ['user_now', ]

    def get_queryset(self, request):
        queries = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queries
        return queries.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            obj.user = str(obj.authors)
        elif obj.user != request.user:
            obj.user = str(request.user)
        if str(obj.authors) == '':
            obj.authors = str(request.user)
        if str(obj.category) == '':
            obj.category = '日记'
        super().save_model(request, obj, form, change)

class CriticismAdmin(admin.ModelAdmin):
    fields = ('article', 'critic', 'portrait_form', 'portrait', 'content', )
    list_display = ['id', 'get_title', 'critic', 'abbr_content', 'pub_date', ]
    readonly_fields = ['portrait_form', ]

    def get_title(self, obj):
        return obj.article.title
    get_title.short_description = '所在文章'
    get_title.admin_order_field = 'article__title'

    def save_model(self, request, obj, form, change):
        if str(obj.critic) == '':
            obj.critic = str(request.user)
        if str(obj.portrait.name) == '':
            obj.portrait.name = os.path.join("portraits", "default.png")
            new_path = os.path.join(settings.MEDIA_ROOT, obj.portrait.name)
            os.rename(obj.portrait.path, new_path)
            obj.save()

            # 我尝试多次失败最后下面成功的代码，效果等同于上面的代码，
            # 通过这个保存头像然后删除并重命名知晓了models.FileField
            # 对应的save会递交upload_to参数，所以解决方法就只是重命名
            # 并使用models.YourModel.save()方法既可
            #with open(os.path.join(settings.MEDIA_ROOT, "portraits", "default.png"), 'rb') as f:
            #    obj.portrait.save("default.png", f, save=False)
            #obj.portrait.delete(save=False)
            #obj.portrait.name = os.path.join("portraits", "default.png")
            #new_path = os.path.join(settings.MEDIA_ROOT, obj.portrait.name)
            #os.rename(obj.portrait.path, new_path)
            #obj.save()
        super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Criticism, CriticismAdmin)
