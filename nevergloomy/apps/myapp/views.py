from apps.myapp.models import Snippet
from apps.myapp.serializers import SnippetSerializer
from apps.myapp.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions

class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def pre_save(self, obj):
		obj.owner = self.request.user

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	def pre_save(self, obj):
		obj.owner = self.request.user

from django.contrib.auth.models import User
from apps.myapp.serializers import UserSerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
