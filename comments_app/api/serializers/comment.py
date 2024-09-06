from rest_framework import serializers

from comments_app.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'user')

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(instance) -> int:
        return instance.likes.count()


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['post']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(instance) -> int:
        return instance.likes.count()
