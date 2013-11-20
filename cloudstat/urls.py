from django.conf.urls import patterns, url, include
# from snippets import views
from thermostats import views
from rest_framework.routers import DefaultRouter

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
router.register(r'thermostats', views.ThermostatViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', 'cloudstat.views.home', name='home'),
    #url(r'^thermostatsDisplay/', include('thermostats.urls', namespace="thermostats")),
)