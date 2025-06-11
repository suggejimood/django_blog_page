from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("posts", views.posts, name="posts-page"),
    path("post/<slug:slug>", views.post, name="post-page"),
]
