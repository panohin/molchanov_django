from email.policy import default
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q


from blog_app.forms import TagForm

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm


def post_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    
    paginator = Paginator(posts, 4)

    
    
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    post_create_url = 'post/create'

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    context = {'title':'Posts',
        'page_object':page,
        'create_template':post_create_url,
        'is_paginated': is_paginated,
        'next_url':next_url,
        'prev_url':prev_url
        }

    return render(request, "blog_app/post_list.html", context=context)


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog_app/post_details.html'
    

def tag_list(request):
    tags = Tag.objects.all()
    tag_create_url = 'tag/create'
    return render(request, 'blog_app/tag_list.html', context={'title':'tag_list' ,'tags':tags, 'create_template':tag_create_url})

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog_app/post_create.html'
    raise_exception = True

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model_name = Post
    form_model = PostForm
    template = 'blog_app/post_update.html'
    raise_exception = True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog_app/post_delete.html'
    raise_exception = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog_app/tag_details.html'
    create_template = 'tag_create_url'
 

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog_app/tag_create.html'
    raise_exception = True
 
class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model_name = Tag
    form_model = TagForm
    template = 'blog_app/tag_update_form.html'
    raise_exception = True
    
class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog_app/tag_delete.html'
    raise_exception = True
    