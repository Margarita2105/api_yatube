from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, CommentViewSet


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',CommentViewSet)

urlpatterns = router.urls

urlpatterns += [
        path('api-token-auth/', views.obtain_auth_token)
    ]
