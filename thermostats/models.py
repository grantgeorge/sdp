from django.db import models

class BaseControl(models.Model):
	account_id = models.IntegerField(default=0)
	basecontrol_id = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	current_temperature = models.IntegerField(default=0)
	setpoint_temperature = models.IntegerField(default=0)
	setback_temperature = models.IntegerField(default=0)
	status = models.BooleanField()

class Thermostat(models.Model):
	base_control = models.ForeignKey(BaseControl)
	account_id = models.IntegerField(default=0)
	thermostat_id = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	current_temperature = models.IntegerField(default=0)
	setpoint_temperature = models.IntegerField(default=0)
	setback_temperature = models.IntegerField(default=0)
	status = models.BooleanField()