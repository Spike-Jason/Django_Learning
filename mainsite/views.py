from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime

# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    for post in posts:
        post_title = post.title

    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
'''
    posts = Post.objects.all()
    print(posts)
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post.title) + "<br>")
        post_lists.append("<small>" + str(post.body) + "</small><br><br>")
    return HttpResponse(post_lists)
'''