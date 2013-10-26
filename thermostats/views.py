from django.http import HttpResponse
from django.template import RequestContext, loader

from thermostats.models import Thermostat

def index(request):
	thermostat_list = Thermostat.objects.order_by('name')[:5]
	template = loader.get_template('thermostats/index.html')
	context = RequestContext(request, {
		'thermostat_list': thermostat_list,
	})
	return HttpResponse(template.render(context))

def detail(request, thermostat_id):
    return HttpResponse("You're looking at thermostat %s." % thermostat_id)

def settings(request, thermostat_id):
    return HttpResponse("You're looking at the settings of thermostat %s." % thermostat_id)

def temperature(request, thermostat_id):
    return HttpResponse("You're looking at the temperature information of thermostat %s." % thermostat_id)