# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No. {}:\t{}<hr>".format(str(count), str(post).decode('utf8')))
        post_lists.append("<small>" + unicode(post.body) + "</small><br><br>")
    return HttpResponse(post_lists)
