from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.shortcuts import render
from datetime import datetime

def Test(request):
    return render(request, 'blog/test.html', {'current_time': datetime.now()})
