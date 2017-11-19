from django.shortcuts import render, redirect
from django.http import Http404

from .models import Post, Tags


# Create your views here.


def index(request):

    posts = Post.objects.all()

    tags = Tags.objects.all()

    return render(request, 'index.html', {'posts':posts, 'tags':tags })


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def post(request, post_id):

    try:
        post = Post.objects.get(id=post_id)

    except DoesNotExist:
        raise Http404()

    return render(request, 'post.html', {'post': post})


def tag(request, tag_id):

    try:

        tag = Tags.objects.get(id = tag_id)

        posts = Post.objects.filter(tags=tag).all()

    except DoesNotExist:

        raise Http404()

    return render(request, 'tag.html', {'tag': tag, 'posts': posts})


def about(request):

    return render(request, 'about.html')


def explore(request):
    return render(request, 'explore.html')


def collections(request):
    return render(request, 'collections.html')
