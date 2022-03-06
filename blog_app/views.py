from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag

def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog_app/post_list.html", context={'title':'post_list' ,'posts':posts})

def post_details(request, slug_from_request):
    post = Post.objects.get(slug=slug_from_request)
    context = {
        'post':post
    }
    return render(request, 'blog_app/post_details.html', context=context)

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog_app/tag_list.html', context={'title':'tag_list' ,'tags':tags})


def tag_details(request, slug_from_request):
    tag = Tag.objects.get(slug=slug_from_request)
    return render(request, 'blog_app/tag_details.html', context={'tag':tag})