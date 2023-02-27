from django.shortcuts import render, redirect

from .function import add_impression_func
from .models import UserPost
from .forms import UserPostForm

template_path = 'main'


def index(request):
    html = f"{template_path}/index.html"
    data = {"title": "Museum in Brhlovce"}
    return render(request, html, context=data)


def history(request):
    html = f"{template_path}/history.html"
    data = {"title": "History"}
    return render(request, html, context=data)


def impression(request):
    html = f"{template_path}/impression.html"
    posts = UserPost.objects.all()
    data = {
        "title": "Impression",
        'posts': posts,
    }
    return render(request, html, data)


def add_impression(request):
    html = f"{template_path}/add_impression.html"
    if request.method == 'GET':
        form = UserPostForm()
        data = {
            "title": "Add Impression",
            'form': form
        }
        return render(request, html, data)
    else:
        add_impression_func(request)
        return redirect('impression')
