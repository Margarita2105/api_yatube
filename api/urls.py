from django.urls import path
from posts.views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('api/v1/posts', PostViewSet)
router.register(r'api/v1/posts/(?P<post_id>\d+)/comments',CommentViewSet)

urlpatterns = router.urls
