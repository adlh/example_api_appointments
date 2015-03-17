from django.core.management.base import BaseCommand

from api.models import Appointment, Participant


class Command(BaseCommand):
    def handle(self, *args, **options):
        owner = Participant.objects.get(name='Andrea')
        participants = ['Bob', 'John', 'Paul', 'Jens', 'Mary']
        appointments = [
            ('An important meeting at the office.', participants[:3]),
            ('Annother meeting at the office.', participants[2:]),
            ('A meeting with everybody.', participants),
        ]
        for text, people in appointments:
            a = Appointment.objects.create(owner=owner, text=text)
            a.participants.add(owner)
            for p in people:
                a.participants.add(Participant.objects.get(name=p))

