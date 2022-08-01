from django.shortcuts import render

from .models import UserPost
from .forms import UserPostForm


def index(request):
    data = {"title": "Obecne muzeum v Brhlovciach"}
    return render(request, "main/index.html", context=data)


def working_hours(request):
    data = {"title": "Working hours"}
    return render(request, 'main/working_hours.html', context=data)


def impression(request):
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
            return render(request, 'main/impression.html', data)
    return render(request, 'main/impression.html', data)


def photo_gallery(request):
    data = {"title": "Photo gallery"}
    return render(request, 'main/photo_gallery.html', context=data)
