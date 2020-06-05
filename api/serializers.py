from rest_framework import serializers

from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()
    
    class Meta:
        fields = '__all__'
        model = Comment