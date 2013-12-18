from django.conf.urls import patterns, url, include
from rest_framework import routers
from apps.myapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# wire up our API using automatic url routing
# additionally we include login urls for the browesable API
urlpatterns = patterns('',
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)