from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        #fields = ['_id', 'game1', 'game2', 'game3', 'game4', 'game5']
        fields = '__all__'

