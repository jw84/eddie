from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.myapp.views import *

# API endpoints
urlpatterns = format_suffix_patterns(patterns('',
	url(r'^$', 'api_root'),
	url(r'^snippets/$', SnippetList.as_view(), name='snippet-list'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view(), name='snippet-detail'),
	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', SnippetHighlight.as_view(), name='snippet-highlight'),
	url(r'^users/$', UserList.as_view(), name='users-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
))
