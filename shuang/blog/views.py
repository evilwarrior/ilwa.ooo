from django.shortcuts import render, render_to_response
from django.http import Http404
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
# 我的模型类
from blog.models import Article
from blog.models import Criticism
from blog.forms import CriticismForm
# python其他模块
import os

def page_not_found(request):
    return render_to_response('404.html')

def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})

def Detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        post_crit = Criticism.objects.filter(article_id__exact=str(id))
        if request.method == 'POST':
            # 检查是否有上传头像
            files = request.FILES
            obj = files.get('portrait')
            flags = False
            if obj is None: flags = True;

            form = CriticismForm(request.POST, files)

            if form.is_valid():
                crit = form.save()
                crit.article_id = id
                # 检查到无上传头像重新上传默认头像
                if flags:
                    with open(os.path.join(settings.MEDIA_ROOT, "portraits", "default.png"), 'rb') as f:
                        crit.portrait.save("default.png", f, save=False)
                    crit.portrait.delete(save=False)
                    crit.portrait.name = os.path.join('portraits', 'default.png')
                    new_path = os.path.join(settings.MEDIA_ROOT, crit.portrait.name)
                    os.rename(crit.portrait.path, new_path)
                    crit.save()
                # 提交表单成功后重定向，防止用户刷新页面重交表单
                return HttpResponseRedirect(reverse('blog_detail', args=(id)))
            else:
                error = form.errors
                return render(request, 'post.html', {'post': post, 'post_crit': post_crit, 'form': form, 'error': error})
        else:
            form = CriticismForm();
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post, 'post_crit': post_crit, 'form': form})

def search_cat(request, cat): #cat(category)在URL中获取
    try:
    #对文章进行过滤，过滤方法是：标签不区分大小写，并且等于tag
        post_list = Article.objects.filter(category__iexact=cat)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'home.html', {'post_list': post_list})

def search_year(request, year): #year在URL中获取
    try:
    #对文章按年份进行归档
        post_list = Article.objects.filter(pub_date__year=year)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'home.html', {'post_list': post_list})

def search_tag(request, tag): #tag在URL中获取
    try:
    #对标签进行过滤
        post_list = Article.objects.filter(tags__contains=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'home.html', {'post_list': post_list})
