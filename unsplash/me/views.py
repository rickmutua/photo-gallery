from django.shortcuts import render, redirect
from .models import Post

# Create your views here.


def index(request):

    posts = Post.

    return render(request, 'index.html', {'posts':posts})


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
