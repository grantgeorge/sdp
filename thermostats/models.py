from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class BaseControl(models.Model):
	account_id = models.IntegerField(default=0)
	basecontrol_id = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	current_temperature = models.IntegerField(default=0)
	setpoint_temperature = models.IntegerField(default=0)
	setback_temperature = models.IntegerField(default=0)
	status = models.BooleanField()
	def __unicode__(self):
		return self.name
	def get_current_temperature(self):
		return self.current_temperature

class Thermostat(models.Model):
	base_control = models.ForeignKey(BaseControl)
	account_id = models.IntegerField(default=0)
	thermostat_id = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	current_temperature = models.IntegerField(default=0)
	setpoint_temperature = models.IntegerField(default=0)
	setback_temperature = models.IntegerField(default=0)
	status = models.BooleanField()
	def __unicode__(self):
		return self.name
	def get_current_temperature(self):
		return self.current_temperature

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly',
                             max_length=100)

    class Meta:
        ordering = ('created',)