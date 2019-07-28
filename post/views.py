from snippets.models import Post
from snippets.serializers import PostSerializer
from rest_framework import generics

# rest_framework/generics.py
# https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py

# ListCreateAPIView
# https://github.com/encode/django-rest-framework/blob/0e1c5d313232a131bb4a1a414abf921744ab40e0/rest_framework/generics.py#L232

# RetrieveUpdateDestroyAPIView
# https://github.com/encode/django-rest-framework/blob/0e1c5d313232a131bb4a1a414abf921744ab40e0/rest_framework/generics.py#L274

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer