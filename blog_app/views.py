from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View


from blog_app.forms import TagForm

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog_app/post_list.html", context={'title':'Posts' ,'posts':posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog_app/post_details.html'
    def get(self, request, slug_from_request):
        post = get_object_or_404(Post, slug=slug_from_request)
        return render(request, 'blog_app/post_details.html', context={'post':post})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog_app/tag_list.html', context={'title':'tag_list' ,'tags':tags})

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog_app/post_create.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog_app/tag_details.html'
    def get(self, request, slug_from_request):
        tag = get_object_or_404(Tag, slug=slug_from_request)
        return render(request, 'blog_app/tag_details.html', context={'tag':tag})

class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog_app/tag_create.html'
 
class TagUpdate(ObjectUpdateMixin, View):
    model_name = Tag
    form_model = TagForm
    template = 'blog_app/tag_update_form.html'
    
    
    # def get(self, request, slug_from_request: str):
    #     tag = Tag.objects.get(slug__iexact=slug_from_request)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog_app/tag_update_form.html', context={'form':bound_form, 'tag':tag})
    # def post(self, request, slug_from_request: str):
    #     tag = Tag.objects.get(slug__iexact=slug_from_request)
    #     bound_form = TagForm(request.POST, instance=tag)

    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog_app/tag_update_form.html', context={'form':bound_form, 'tag':tag})