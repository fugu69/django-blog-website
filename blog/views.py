from django.shortcuts import render, get_object_or_404
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_details.html", {"post": post})
