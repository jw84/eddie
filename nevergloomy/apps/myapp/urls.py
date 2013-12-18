from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.myapp.views',
	url(r'^snippets/$', 'snippet_list'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)

