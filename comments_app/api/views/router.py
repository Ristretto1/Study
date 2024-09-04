from rest_framework import routers

from comments_app.api.views.comment import CommentViewSet

api_router = routers.DefaultRouter()
api_router.register('comments', CommentViewSet)
# api_router.register('posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments_of_posts')