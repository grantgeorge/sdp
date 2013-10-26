from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from thermostats.models import Thermostat

def index(request):
	thermostat_list = Thermostat.objects.order_by('name')[:5]
	context = {'thermostat_list': thermostat_list}
	return render(request, 'thermostats/index.html', context)

def detail(request, in_id):
	thermostat = get_object_or_404(Thermostat, pk=in_id)
	return render(request, 'thermostats/detail.html', {'thermostat': thermostat})

def settings(request, thermostat_id):
    return HttpResponse("You're looking at the settings of thermostat %s." % thermostat_id)

def temperature(request, thermostat_id):
    return HttpResponse("You're looking at the temperature information of thermostat %s." % thermostat_id)