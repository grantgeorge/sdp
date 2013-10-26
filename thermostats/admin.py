from django.contrib import admin
from thermostats.models import BaseControl, Thermostat

admin.site.register(Thermostat)
admin.site.register(BaseControl)