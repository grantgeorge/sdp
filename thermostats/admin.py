from django.contrib import admin
from thermostat.models import BaseControl, Thermostat

admin.site.register(Thermostat)
admin.site.register(BaseControl)