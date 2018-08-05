from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime

# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

    # post_lists = list() #建立空表
    # for count, post in enumerate(posts):
    #     post_lists.append("No.{}:".format(str(count))+str(post.title)+"<br>")
    #     # <small>标签,在html中定义小型文本
    #     post_lists.append("<small>" + str(post.body) + "</small><br><br>")
    # return HttpResponse(post_lists)
