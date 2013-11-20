from rest_framework import serializers
from thermostats.models import Thermostat
from django.contrib.auth.models import User


class ThermostatSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='thermostat-highlight', format='html')

    class Meta:
        model = Thermostat
        fields = ('url', 'highlight', 'owner',
                  'created', 'name', 'account_id', 'current_temperature', 'setpoint_temperature',
                  'setback_temperature')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    thermostats = serializers.ManyHyperlinkedRelatedField(view_name='thermostat-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'thermostats')