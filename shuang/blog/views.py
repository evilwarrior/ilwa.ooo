from django.shortcuts import render
from blog.models import Article
from datetime import datetime
from django.http import Http404

def page_not_found(request):
    return render_to_response('404.html')

def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})

def Detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})

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
