from rest_framework import generics, permissions

from .serializers import AppointmentSerializer
from .models import Appointment

class AppointmentDetail(generics.RetrieveAPIView):
    model = Appointment
    serializer_class = AppointmentSerializer
    #permission_classes = [
        #permissions.AllowAny
    #]
    lookup_field = 'pk'
    queryset = Appointment.objects.all()

