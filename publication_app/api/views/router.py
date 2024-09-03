from rest_framework import routers

from publication_app.api.views.post import PostViewSet

api_router = routers.DefaultRouter()
api_router.register('posts', PostViewSet)
