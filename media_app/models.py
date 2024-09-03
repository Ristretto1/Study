from django.contrib.auth.models import User
from django.db import models


class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    file = models.ImageField(blank=False, null=False, upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
