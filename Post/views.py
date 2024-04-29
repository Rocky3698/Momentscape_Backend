from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class PostViewset(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        queryset = super().get_queryset() 
        print(self.request.query_params)
        post_id = self.request.query_params.get('post_id')
        user_id = self.request.query_params.get('user_id')
        if post_id:
            queryset = queryset.filter(id=post_id)
        elif user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

class ReactViewset(viewsets.ModelViewSet):
    queryset = models.React.objects.all()
    serializer_class = serializers.ReactSerializer

    def get_queryset(self):
        queryset = super().get_queryset() 
        print(self.request.query_params)
        post_id = self.request.query_params.get('post_id')
        like = self.request.query_params.get('like')
        if like =='true':like=True
        
        if post_id:
            queryset = queryset.filter(post_id=post_id)
            if like:
                queryset = queryset.filter(like=like)
        return queryset

class CommentViewset(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        queryset = super().get_queryset() 
        print(self.request.query_params)
        post_id = self.request.query_params.get('post_id')
        
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        return queryset