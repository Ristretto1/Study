from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from media_app.api.serializers.media import MediaSerializer
from media_app.models import Media


class MediaViewSet(GenericViewSet, RetrieveModelMixin, CreateModelMixin):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
