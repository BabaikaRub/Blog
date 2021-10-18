from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Post


class MainView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "index.html"


class PostDetailView(DetailView):
    model = Post
    slug_field = 'url'
    template_name = "post.html"
