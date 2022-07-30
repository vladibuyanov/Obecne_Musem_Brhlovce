from django.shortcuts import render

from main_app.models import UserPosts


def index(request):
    data = {"title": "Obecne muzeum v Brhlovciach"}
    return render(request, "main/index.html", context=data)


def working_hours(request):
    data = {"title": "Working hours"}
    return render(request, 'main/working_hours.html', context=data)


def impression(request):
    posts = UserPosts.objects.all()
    if request.method == "POST":
        UserPosts.objects.create(
            name=request.POST.get('name'),
            post=request.POST.get('post'),
        )
        return render(request, 'main/impression.html', {'posts': posts})
    return render(request, 'main/impression.html', {'posts': posts})


def photo_gallery(request):
    return render(request, 'main/photo_gallery.html')
