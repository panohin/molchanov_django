from operator import mod
from statistics import mode
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(path_to_slug: str) -> str:
    '''Generate slug from title'''
    slug = slugify(path_to_slug, allow_unicode=True)
    return slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_published = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'slug_from_request':self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug_from_request':self.slug})
    
    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)    

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    def get_absolute_url(self):
        return reverse('tag_details_url', kwargs={'slug_from_request':self.slug})
    
    def __str__(self) -> str:
        return self.title

    