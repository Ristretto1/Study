from django.db.models.signals import post_save
from django.dispatch import receiver

from likes_app.models import Like


@receiver(post_save, sender=Like)
def func(sender, instance, **kwargs):
    if instance.post:
        instance.post.who_liked.add(instance.user)
    if instance.comment:
        instance.comment.who_liked.add(instance.user)
