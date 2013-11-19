# from django.conf.urls import patterns, url

# from thermostats import views

# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index'),
#     # ex: /thermostats/5/
#     url(r'^(?P<thermostat_id>\d+)/$', views.detail, name='detail'),
#     # ex: /thermostats/5/settings/
#     url(r'^(?P<thermostat_id>\d+)/settings/$', views.settings, name='settings'),
#     # ex: /thermostats/5/temperature/
#     url(r'^(?P<thermostat_id>\d+)/temperature/$', views.temperature, name='temperature'),
# )

from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from thermostats.views import ThermostatViewSet, UserViewSet
from rest_framework import renderers

# API endpoints
urlpatterns = format_suffix_patterns(patterns('thermostats.views',
    url(r'^$', 'api_root'),
    url(r'^thermostats/$', thermostat_list, name='thermostat-list'),
    url(r'^thermostats/(?P<pk>[0-9]+)/$', thermostat_detail, name='thermostat-detail'),
    url(r'^thermostats/(?P<pk>[0-9]+)/highlight/$', thermostat_highlight, name='thermostat-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
))

# Login and logout views for the browsable API
urlpatterns += patterns('',    
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

thermostat_list = ThermostatViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
thermostat_detail = ThermostatViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
thermostat_highlight = ThermostatViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})