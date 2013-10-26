from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the thermostat index.")

def detail(request, thermostat_id):
    return HttpResponse("You're looking at thermostats %s." % thermostat_id)

def settings(request, thermostat_id):
    return HttpResponse("You're looking at the settings of thermostat %s." % thermostat_id)

def temperature(request, thermostat_id):
    return HttpResponse("You're temperature information on thermostat %s." % thermostat_id)