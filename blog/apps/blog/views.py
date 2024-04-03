from django.shortcuts import render
from django.http import Http404

from .models import Post


def index(request):
    posts = Post.objects_active.all()
    return render(
        request,
        'blog/index.html',
        {
            'articles': posts
        }
    )


def post_detail(request, slug):
    try:
        post = Post.objects_active.get(slug=slug)

    except Post.DoesNotExist:
        raise Http404

    return render(
        request,
        'blog/post.html',
        {
            'article': post
        }
    )
