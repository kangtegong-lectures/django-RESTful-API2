from post.models import Post
from post.serializer import PostSerializer

from rest_framework import viewsets

# @action처리
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

'''
# ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 조회만 가능

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


'''
# ModelViewSet은 ListView와 DetailView에 대한 CRUD가 모두 가능

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # @action(method=['post'])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 얍을 띄우는 custom api
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍")
