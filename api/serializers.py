from rest_framework import serializers

from .models import Appointment, Participant, ScheduleOption, AcceptedOption

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('id', 'name', 'email')


class AcceptedOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedOption
        fields = ('id', 'option', 'participant')


class AppointmentSerializer(serializers.ModelSerializer):
    owner = ParticipantSerializer()
    class Meta:
        model = Appointment
        depth = 1
        fields = ('id', 'owner', 'text', 'participants', 'options', 'best_options',
                'option_overview')

class AppointmentListSerializer(serializers.ModelSerializer):
    details = serializers.HyperlinkedIdentityField(view_name='appointment-view')
    class Meta:
        model = Appointment
        fields = ('owner', 'text', 'details')

