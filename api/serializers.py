from rest_framework import serializers

from .models import Appointment, Participant, ScheduleOption, AcceptedOption

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('text', 'best_options', 'option_overview')
