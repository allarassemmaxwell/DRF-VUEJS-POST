from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    cat_name = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Post
        fields = [
            'cat_name',
            'id',
            'title',
            'content',
            'timestamp'    
        ]
        
