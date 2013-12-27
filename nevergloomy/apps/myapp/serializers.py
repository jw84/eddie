from django.forms import widgets
from rest_framework import serializers
from apps.myapp.models import Event
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	events = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail')
	#snippets = serializers.PrimaryKeyRelatedField(many=True)

	class Meta:
		model = User
		fields = ('url', 'username', 'events')

class EventSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.Field(source='owner.username')

	class Meta:
		model = Event
		fields = ('url', 'link', 'title', 'showtime', 'description', 'created', 'owner')

	def restore_object(self, attrs, instance=None):
		"""
		Create or update a new event instance, given a dictionary of deserialized field values.
		Note that if we don't define this method, then deserializing data will simply return a dictionary of items.
		"""
		if instance:
			# Update existing instance
			instance.link = attrs.get('title', instance.link)
			instance.showtime = attrs.get('time', instance.showtime)
			instance.description = attrs.get('desc', instance.description)
			instance.created = attrs.get('created', instance.created)
			instance.owner = attrs.get('owner', instance.owner)
			return instance

		# Create new instance
		return Event(**attrs)
