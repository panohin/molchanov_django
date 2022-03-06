from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tags/', views.tag_list, name='tag_list'),
    path('post/<str:slug_from_request>', views.post_details, name='post_details'),
    path('tag/<str:slug_from_request>', views.tag_details, name='tag_details_url')
]
