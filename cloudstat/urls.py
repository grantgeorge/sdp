from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Import thermostat model
from thermostats.models import Thermostat, BaseControl

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

# Thermostat define the view behavior.
class ThermostatsViewSet(viewsets.ModelViewSet):
	model = Thermostat

# # Routers provide an easy way of automatically determining the URL conf
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'thermostatcall', ThermostatsViewSet)

urlpatterns = patterns('',
	# REST
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    # Examples:
    # url(r'^$', 'cloudstat.views.home', name='home'),
    # url(r'^cloudstat/', include('cloudstat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', 'cloudstat.views.home', name='home'),
    url(r'^thermostats/', include('thermostats.urls', namespace="thermostats")),
    url(r'^', include('snippets.urls')), 
)
