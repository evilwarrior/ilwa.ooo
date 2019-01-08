from django.shortcuts import render
from blog.models import Article
from datetime import datetime
from django.http import Http404

def page_not_found(request):
    return render_to_response('404test.html')

def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})

def Detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})
