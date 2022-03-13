from pyexpat import model
from django.shortcuts import render, get_object_or_404, redirect

from .models import Tag, Post

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug_from_request):
        object = get_object_or_404(self.model, slug=slug_from_request)
        return render(request, self.template, context={self.model.__name__.lower():object})

class ObjectCreateMixin:
    form_model = None
    template = None
    
    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form':form})
    
    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, self.template, context={'form':bound_form})
