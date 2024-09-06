from rest_framework import serializers

from comments_app.api.serializers.comment import CommentDetailSerializer
from media_app.api.serializers.media import MediaSerializer
from project.api.serializers.user import UserSerializer
from publication_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['is_public']
        read_only_fields = ('id', 'user', 'is_public')

        # extra_kwargs = {'media': {'required': True, 'write_only': True, 'help_text': 'Media file'}}

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    # media = serializers.URLField(source='file.file.url', read_only=True)
    media = MediaSerializer(source='file', allow_null=False, read_only=True)
    comments = CommentDetailSerializer(many=True, allow_null=False, read_only=True)
    likes = serializers.SerializerMethodField()
    who_liked = UserSerializer(many=True, read_only=True)

    @staticmethod
    def get_likes(instance):
        return instance.likes.count()
