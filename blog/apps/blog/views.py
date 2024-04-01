from django.shortcuts import render

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
    post = Post.objects_active.get(slug=slug)
    return render(
        request,
        'blog/post.html'
    )
