from django.contrib import admin
from thermostats.models import BaseControl, Thermostat

class BaseControlAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['account_id', 'basecontrol_id', 'name']}),
		('Temperature Information', {'fields':['current_temperature', 'setpoint_temperature', 'setback_temperature', 'status']}),
	]
	list_display = ('name', 'account_id', 'basecontrol_id')
	search_fields = ['name']

class ThermostatAdmin(admin.ModelAdmin):
	fields = ['base_control', 'account_id', 'thermostat_id', 'name', 'current_temperature', 'setpoint_temperature', 'setback_temperature', 'status']

admin.site.register(BaseControl, BaseControlAdmin)
admin.site.register(Thermostat, ThermostatAdmin)