from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import Appointment, Participant, AcceptedOption

from pprint import pformat

import logging

logger = logging.getLogger(__name__)

class AppointmentDetail(generics.RetrieveAPIView):
    model = Appointment
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class AppointmentList(generics.ListAPIView):
    model = Appointment
    serializer_class = AppointmentListSerializer
    queryset = Appointment.objects.all()


class ParticipantDetail(generics.RetrieveAPIView):
    model = Participant
    serializer_class = ParticipantSerializer
    lookup_field = 'pk'
    queryset = Participant.objects.all()


class AcceptedList(generics.ListAPIView):
    model = AcceptedOption
    serializer_class = AcceptedOptionSerializer

    def get_queryset(self):
        qset = AcceptedOption.objects.filter(
                option__appointment__id=self.kwargs['appointment'],
                participant__id=self.kwargs['participant'])
        return qset


# Use a function based view to update the accepted options for a specific
# participant and appointment
@api_view(['GET', 'POST'])
def update_accepted_view(request, appointment, participant):
    if request.method == 'POST':
        d = request.data
        #logger.debug(pformat({'data': d}))
        # sanitize data (should only be id's)
        app_id = int(d.get('appointment', 0))
        p_id = int(d.get('participant', 0))
        options = [int(o) for o in d.get('options', [])]
        participant = Participant.objects.get(pk=p_id)
        participant.update_accepted(app_id, options)
        return Response({"message": "Options update successfully!"})
    return Response({"message": "Hello, world!"})

