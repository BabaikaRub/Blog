from django.shortcuts import render
from django.views import View

from .models import Post


class MainView(View):
    def get(self, request):
        # posts = Post.objects.all()
        return render(request, "index.html", {})


class PostView(View):
    def get(self, request):
        return render(request, 'post.html', {})
