from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, "blog_app/post_list.html", context={'hello':'hi'})
