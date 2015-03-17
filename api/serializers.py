from rest_framework import serializers

from .models import Appointment, Participant, ScheduleOption, AcceptedOption

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('name', 'email')


class AppointmentSerializer(serializers.ModelSerializer):
    owner = ParticipantSerializer()
    class Meta:
        model = Appointment
        fields = ('owner', 'text', 'best_options', 'option_overview')
