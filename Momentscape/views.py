from django.contrib.auth.models import User 

from rest_framework import viewsets
from . import serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    def get_queryset(self):
        queryset = super().get_queryset() 
        print(self.request.query_params)
        user_id = self.request.query_params.get('user_id')
        
        if user_id:
            queryset = queryset.filter(id=user_id)
        return queryset