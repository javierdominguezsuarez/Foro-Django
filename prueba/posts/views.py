from django.shortcuts import render
from rest_framework import viewsets
from posts.serializers import PostSerializer
from posts.models import Post



def lista_post(request):
	lista_post= Post.objects.all()
	return render(request, 'listaPosts.html', {"posts": lista_post})

class PostViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    