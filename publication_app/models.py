from django.contrib.auth.models import User
from django.db import models
from django.db.models import DateField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    created_at = DateField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
