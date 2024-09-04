from django.contrib.auth.models import User
from django.db import models

from publication_app.models import Post


# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name='comments')
