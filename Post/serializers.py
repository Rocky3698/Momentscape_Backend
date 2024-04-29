from rest_framework import serializers
from .models import Post,Comment,React

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = '__all__'