from django.contrib import admin
from thermostats.models import BaseControl, Thermostat

class BaseControlAdmin(admin.ModelAdmin):
	fields = ['account_id', 'basecontrol_id', 'name', 'current_temperature', 'setpoint_temperature', 'setback_temperature', 'status']

class ThermostatAdmin(admin.ModelAdmin):
	fields = ['base_control', 'account_id', 'thermostat_id', 'name', 'current_temperature', 'setpoint_temperature', 'setback_temperature', 'status']

admin.site.register(BaseControl, BaseControlAdmin)
admin.site.register(Thermostat, ThermostatAdmin)