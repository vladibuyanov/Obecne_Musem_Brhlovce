from app.forms import UserPostForm


def add_impression_func(request):
    new_post = UserPostForm(request.POST)
    if new_post.is_valid():
        new_post.save()
