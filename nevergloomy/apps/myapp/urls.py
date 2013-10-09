from django.conf.urls import patterns, url

from apps.myapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)