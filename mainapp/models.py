from django.db import models


# Create your models here.
class UserPosts(models.Model):
    name = models.CharField(max_length=20, default="Anonim")
    post = models.TextField(null=False)
    time = models.DateTimeField()

    def __str__(self):
        return self.name
