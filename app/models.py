from django.utils import timezone
from django.db import models


class UserPost(models.Model):
    """
        Model of users post
    """
    name = models.CharField(max_length=20, default="Anonim")
    post = models.TextField(null=False)
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'User Post'
        verbose_name_plural = 'User Posts'

    def __str__(self):
        return f'Post of {self.name}'
