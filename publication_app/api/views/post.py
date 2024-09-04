from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from comments_app.api.serializers.comment import CommentSerializer
from comments_app.models import Comment
from publication_app.api.serializers.post import PostSerializer
from publication_app.models import Post


class PostViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                  DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'id']

    # @action(detail=False, methods=['GET'])
    # def comments(self, request, pk=None):
    #     comments = Comment.objects.filter(post_id=pk)
    #     return Response(data=CommentSerializer(comments, many=True).data)

