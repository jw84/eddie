from apps.myapp.models import Event
from django.contrib.auth.models import User
from apps.myapp.serializers import EventSerializer, UserSerializer
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
		'events': reverse('events-list', request=request, format=format)
	})

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides list and detail actions.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides list, create, retrive, update, and destroy actions.
	
	Additionally we also provide an extra highlight action
	"""
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	def pre_save(self, obj):
		obj.owner = self.request.user
