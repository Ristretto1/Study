from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from likes_app.api.serializers.like import LikeSerializer
from likes_app.models import Like


class LikeViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()