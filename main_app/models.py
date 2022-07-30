import datetime
from django.db import models


# Create your models here.
class UserPosts(models.Model):
    """
        Model of users post
    """
    verbose_name = 'User posts'

    name = models.CharField(max_length=20, default="Anonim")
    post = models.TextField(null=False)
    time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'Post of {self.name}'
