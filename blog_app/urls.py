from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tags/', views.tag_list, name='tag_list'),
    path('post/create', views.PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug_from_request>', views.PostDetail.as_view(), name='post_details'),
    path('post/<str:slug_from_request>/update', views.PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug_from_request>/delete', views.PostDelete.as_view(), name='post_delete_url'),
    path('tags/tag/create', views.TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug_from_request>/update', views.TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug_from_request>/delete', views.TagDelete.as_view(), name='tag_delete_url'),
    path('tag/<str:slug_from_request>', views.TagDetail.as_view(), name='tag_details_url'),
    
]
