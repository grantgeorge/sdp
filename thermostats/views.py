# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404

# from thermostats.models import Thermostat

# def index(request):
# 	thermostat_list = Thermostat.objects.order_by('name')[:5]
# 	context = {'thermostat_list': thermostat_list}
# 	return render(request, 'thermostats/index.html', context)

# def detail(request, thermostat_id):
# 	thermostat = get_object_or_404(Thermostat, pk=thermostat_id)
# 	return render(request, 'thermostats/detail.html', {'thermostat': thermostat})

# def settings(request, thermostat_id):
#     return HttpResponse("You're looking at the settings of thermostat %s." % thermostat_id)

# def temperature(request, thermostat_id):
#     return HttpResponse("You're looking at the temperature information of thermostat %s." % thermostat_id)

from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
from thermostats.models import Thermostat
from thermostats.permissions import IsOwnerOrReadOnly
from thermostats.serializers import ThermostatSerializer, UserSerializer

class ThermostatViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code thermostats.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code thermostat.

    The **owner** of the code thermostat may update or delete instances
    of the code thermostat.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Thermostat.objects.all()
    serializer_class = ThermostatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @link(renderer_classes=(renderers.StaticHTMLRenderer,))
    def highlight(self, request, *args, **kwargs):
        thermostat = self.get_object()
        return Response(thermostat.highlighted)

    def pre_save(self, obj):
        obj.owner = self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.

    As you can see, the collection of thermostat instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer