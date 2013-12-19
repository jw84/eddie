from apps.myapp.models import Snippet
from django.contrib.auth.models import User
from apps.myapp.serializers import SnippetSerializer, UserSerializer
from apps.myapp.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, link
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import renderers

@api_view(('GET',))
def api_root(Request, format=None):
	return Response({
		'user': reverse('user-list', request=request, format=format),
		'snippets': reverse('snippet-list', request=request, format=format)
	})

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides list and detail actions.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides list, create, retrive, update, and destroy actions.
	
	Additionally we also provide an extra highlight action
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	@link(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def pre_save(self, obj):
		obj.owner = self.request.user
