from django.conf.urls import patterns, url, include
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

from thermostats import views

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
	# REST
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # INDEX
    url(r'^$', views.index, name='index'),
    # ex: /thermostats/5/
    url(r'^(?P<thermostat_id>\d+)/$', views.detail, name='detail'),
    # ex: /thermostats/5/settings/
    url(r'^(?P<thermostat_id>\d+)/settings/$', views.settings, name='settings'),
    # ex: /thermostats/5/temperature/
    url(r'^(?P<thermostat_id>\d+)/temperature/$', views.temperature, name='temperature'),
    
)