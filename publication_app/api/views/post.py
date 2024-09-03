from rest_framework import filters
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from publication_app.api.serializers.post import PostSerializer
from publication_app.models import Post


class PostViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                  DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'id']
