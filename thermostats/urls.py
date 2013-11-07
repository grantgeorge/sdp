from django.conf.urls import patterns, url

from thermostats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /thermostats/5/
    url(r'^(?P<thermostat_id>\d+)/$', views.detail, name='detail'),
    # ex: /thermostats/5/settings/
    url(r'^(?P<thermostat_id>\d+)/settings/$', views.settings, name='settings'),
    # ex: /thermostats/5/temperature/
    url(r'^(?P<thermostat_id>\d+)/temperature/$', views.temperature, name='temperature'),
)