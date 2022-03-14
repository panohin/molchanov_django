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

class ObjectUpdateMixin:
    model_name = None
    form_model = None
    template = None
    
    def get(self, request, slug_from_request: str):
        model_name = self.model_name()
        object = model_name.objects.get(slug__iexact=slug_from_request)
        bound_form = form_model(instance=object)
        return render(request, self.template, context={'form':bound_form, 'object':object})
    
    def post(self, request, slug_from_request: str):
        model_name = self.model_name()
        object = model_name.objects.get(slug__iexact=slug_from_request)
        bound_form = self.form_model(request.POST, instance=object)

        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        return render(request, self.template, context={'form':bound_form, 'object':object})


