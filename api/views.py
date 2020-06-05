from rest_framework import viewsets, serializers, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permission import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])
