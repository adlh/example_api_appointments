from django.test import TestCase
from .models import Appointment


class AppointmentsTestCase(TestCase):
    fixtures = ['appointments_testdata.json']

    def test_appointments_created(self):
      self.assertEqual(len(Appointment.objects.all()), 3)


    def test_best_options(self):
        a1 = Appointment.objects.get(pk=1)
        last_best = None
        # Check that best_options are ordered by count (DESC)
        cnt = 0
        for b in a1.best_options:
            cnt += 1
            if last_best:
                self.assertTrue(b.count <= last_best.count)
            last_best = b
        self.assertEqual(cnt, 3)


    def test_empty_best_options(self):
        a_empty = Appointment.objects.get(pk=2)
        # If no option has been accepted for this appointment, best_options
        # should return an empty array
        self.assertEqual(a_empty.best_options, [])
        # And the option overview should have 3 elements (without participants)
        self.assertEqual(len(a_empty.option_overview), 3)


