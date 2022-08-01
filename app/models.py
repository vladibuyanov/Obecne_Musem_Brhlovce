import datetime
from django.db import models


class UserPost(models.Model):
    """
        Model of users post
    """
    class Meta:
        verbose_name = 'User Post'
        verbose_name_plural = 'User Posts'

    name = models.CharField(max_length=20, default="Anonim")
    post = models.TextField(null=False)
    time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'Post of {self.name}'
