from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

from thermostats.models import Thermostat

def index(request):
	thermostat_list = Thermostat.objects.order_by('name')[:5]
	context = {'thermostat_list': thermostat_list}
	return render(request, 'thermostats/index.html', context)

def detail(request, thermostat_id):
	try:
		thermostat = Thermostat.objects.get(pk=thermostat_id)
	except Thermostat.DoesNotExist:
		raise Http404
	return render(request, 'thermostats/detail.html', {'thermostat': thermostat})

def settings(request, thermostat_id):
    return HttpResponse("You're looking at the settings of thermostat %s." % thermostat_id)

def temperature(request, thermostat_id):
    return HttpResponse("You're looking at the temperature information of thermostat %s." % thermostat_id)