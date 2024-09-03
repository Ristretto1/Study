from rest_framework import routers

from media_app.api.views.media import MediaViewSet

api_router = routers.DefaultRouter()
api_router.register('media', MediaViewSet)
