from django.shortcuts import render

from .models import UserPost
from .forms import UserPostForm


def index(request):
    html = "main/index.html"
    data = {"title": "Museum in Brhlovce"}
    return render(request, html , context=data)


def history(request):
    html = 'main/history.html'
    data = {"title": "History"}
    return render(request, html, context=data)


def impression(request):
    html = 'main/impression.html'
    posts = UserPost.objects.all()
    form = UserPostForm()
    data = {
        "title": "Impression",
        'posts': posts,
        'form': form
    }
    if request.method == "POST":
        new_post = UserPostForm(request.POST)
        if new_post.is_valid():
            new_post.save()
            return render(request, html, data)
    return render(request, html, data)
