from django.shortcuts import render, redirect
from django.http import Http404

from .models import Post, Tags
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.


def index(request):

    try:

        posts = Post.objects.all()

        tags = Tags.objects.all()

    except ObjectDoesNotExist:

        raise Http404()

    return render(request, 'index.html', {'posts':posts, 'tags':tags })


def search_results(request):

    if 'tag' in request.GET and request.GET['tag']:
        search_term = request.GET.get('tag')
        searched_tags = Tags.search_by_tag(search_term)

        posts = Post.objects.filter(tags= searched_tags).all()


    else:
        message = "You haven't searched for any term"
        return render(request, 'searched-tag.html', {"message": message, 'posts': posts})


def post(request, post_id):

    try:
        post = Post.objects.get(id=post_id)
        gotten_tags = post.tags.all()

        related_tag = gotten_tags[0]

        related_images = Post.objects.filter(tags = related_tag).all()

    except DoesNotExist:
        raise Http404()

    return render(request, 'post.html', {'post': post, 'related_images': related_images})


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
