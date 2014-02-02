from rest_framework import generics
from models import Post
from serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
	"""
	List all boards, or create a new board.
	"""
	model = Post
	serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a board instance.
	"""
	model = Post
	serializer_class = PostSerializer
