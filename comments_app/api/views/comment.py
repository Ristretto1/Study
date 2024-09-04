from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from comments_app.api.serializers.comment import CommentSerializer
from comments_app.models import Comment


class CommentViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()