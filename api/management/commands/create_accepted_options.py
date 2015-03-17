from django.core.management.base import BaseCommand

from api.models import ScheduleOption, Appointment, AcceptedOption


class Command(BaseCommand):
    def handle(self, *args, **options):
        a1 = Appointment.objects.get(pk=1)
        # a1 has participants: Andrea, Bob, John, Paul
        andrea = a1.participants.get(name='Andrea')
        bob = a1.participants.get(name='Bob')
        john = a1.participants.get(name='John')
        paul = a1.participants.get(name='Paul')
        # Andrea accepts all 3 options
        accept_options(a1, andrea, [1, 2, 3])
        # Bob accepts option 3
        accept_options(a1, bob, [3])
        # John accepts option 2
        accept_options(a1, john, [2])
        # Paul accepts options 1 and 3
        accept_options(a1, paul, [1, 3])


def accept_options(appointment, participant, pk_lst):
    for pk in pk_lst:
        option = appointment.options.get(pk=pk)
        AcceptedOption.objects.create(participant=participant, option=option)

