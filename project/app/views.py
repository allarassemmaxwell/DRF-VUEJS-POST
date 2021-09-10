from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
# Create your views here.




def home(request):
    return render(request, 'home.html', {})

class postsView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
