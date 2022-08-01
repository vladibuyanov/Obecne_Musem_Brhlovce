from .models import UserPost
from django.forms import ModelForm, TextInput, Textarea


class UserPostForm(ModelForm):
    class Meta:
        model = UserPost
        fields = ['name', 'post']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Dojem'}),
            'post': Textarea(attrs={'placeholder': 'Napíšte svoje dojmy'})
        }
