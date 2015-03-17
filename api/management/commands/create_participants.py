from django.core.management.base import BaseCommand

from api.models import Participant


class Command(BaseCommand):
    def handle(self, *args, **options):
        participants = [
            ('Andrea', 'info@metamorfosy.de'),
            ('Bob', 'bob@example.de'),
            ('John', 'john@example.de'),
            ('Paul', 'paul@example.de'),
            ('Jens', 'jens@example.de'),
            ('Mary', 'mary@example.de')]
        for name, email in participants:
            Participant.objects.create(name=name, email=email)
