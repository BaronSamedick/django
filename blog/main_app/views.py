from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from main_app.models import Post
from main_app.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def posts(request):
    return render(request, 'index.html')
