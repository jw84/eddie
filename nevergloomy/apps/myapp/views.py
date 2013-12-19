from apps.myapp.models import Snippet
from apps.myapp.serializers import SnippetSerializer
from apps.myapp.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(Request, format=None):
	return Response({
		'user': reverse('user-list', request=request, format=format),
		'snippets': reverse('snippet-list', request=request, format=format)
	})

class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippet.objects.all()
	renderer_classes = (renderers.StaticHTMLRenderer,)

	def get(self, request, *Args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

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
