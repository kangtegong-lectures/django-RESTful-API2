# 데이터 처리 대상 : 모델, Serializer import 시키기
from post.models import Post
from post.serializer import PostSerializer

from rest_framework import generics
from rest_framework import mixins

# mixin 직접 보기 : https://github.com/encode/django-rest-framework/blob/master/rest_framework/mixins.py
# genericAPIView 직접 보기 : https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py

class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, 
                generics.GenericAPIView):
    queryset = Post.objects.all()   # 쿼리셋 등록!
    serializer_class = PostSerializer # Serializer 클래스 등록!

    # get은 list메소드를 내보내는 메소드
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # post는 create을 내보내는 메소드
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # DetailView의 get은 retrieve을 내보내는 메소드
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # put은 update을 내보내는 메소드
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # delete은 destroy를 내보내는 메소드
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
