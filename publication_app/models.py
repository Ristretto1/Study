from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.db import models
from django.db.models import DateField
from rest_framework import serializers

from media_app.models import Media


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    created_at = DateField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    file = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    comments = serializers.SerializerMethodField()

    def get_comments(self, instance):
        return instance.comments.all()
