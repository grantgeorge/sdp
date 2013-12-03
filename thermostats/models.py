from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments import highlight

# class BaseControl(models.Model):
# 	account_id = models.IntegerField(default=0)
# 	basecontrol_id = models.IntegerField(default=0)
# 	name = models.CharField(max_length=200)
# 	current_temperature = models.IntegerField(default=0)
# 	setpoint_temperature = models.IntegerField(default=0)
# 	setback_temperature = models.IntegerField(default=0)
# 	status = models.BooleanField()
# 	def __unicode__(self):
# 		return self.name
# 	def get_current_temperature(self):
# 		return self.current_temperature

# comment

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Thermostat(models.Model):
	# base_control = models.ForeignKey(BaseControl)
	created = models.DateTimeField(auto_now_add=True)
	account_id = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	code = models.TextField()
	language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
	current_temperature = models.IntegerField(default=0)
	setpoint_temperature = models.IntegerField(default=0)
	setback_temperature = models.IntegerField(default=0)
	status = models.BooleanField(default=False)
	owner = models.ForeignKey('auth.User', related_name='thermostats')
	highlighted = models.TextField()
	class Meta:
		ordering = ('created',)
	def save(self, *args, **kwargs):
		"""
		Use the `pygments` library to create a highlighted HTML
		representation of the code snippet.
		"""
		status = self.status and 'table' or False
		options = self.name and {'name': self.name} or {}
		lexer = get_lexer_by_name(self.language)
		formatter = HtmlFormatter(current_temperature=self.current_temperature, status=status,
		                          full=True, **options)
		self.highlighted = highlight(self.code, lexer, formatter)
		super(Thermostat, self).save(*args, **kwargs)

		# limit the number of instances retained
		thermostats = Thermostat.objects.all()
		if len(thermostats) > 1000:
			thermostats[0].delete()
	def __unicode__(self):
		return self.name
	def get_current_temperature(self):
		return self.current_temperature