from django.http import HttpResponse
from django.shortcuts import render

from thermostats.models import Thermostat

def index(request):
	thermostat_list = Thermostat.objects.order_by('name')[:5]
	context = {'thermostat_list': thermostat_list}
	return render(request, 'thermostats/index.hmlt', context)

def detail(request, thermostat_id):
    return HttpResponse("You're looking at thermostat %s." % thermostat_id)

def settings(request, thermostat_id):
    return HttpResponse("You're looking at the settings of thermostat %s." % thermostat_id)

def temperature(request, thermostat_id):
    return HttpResponse("You're looking at the temperature information of thermostat %s." % thermostat_id)