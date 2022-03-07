from operator import mod
from statistics import mode
from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_published = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'slug_from_request':self.slug})
    
    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    def get_absolute_url(self):
        return reverse('tag_details_url', kwargs={'slug_from_request':self.slug})
    
    def __str__(self) -> str:
        return self.title

    