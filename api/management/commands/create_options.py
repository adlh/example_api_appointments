from django.core.management.base import BaseCommand
import pytz
from datetime import datetime as dt, timedelta as td
#from django.utils.timezone import timedelta as td, datetime as dt, now

from api.models import ScheduleOption, Appointment


class Command(BaseCommand):
    def handle(self, *args, **options):
        appointments = Appointment.objects.all()
        # use timezone aware datetimes
        ltz = pytz.timezone('Europe/Berlin')
        today = ltz.localize(dt.now())
        # lets start with today at 8 for creating dates and then make a set of
        # options for each appointment (3) of a day with different times
        base = ltz.localize(dt(today.year, today.month, today.day, 8))
        days = [base + td(7), base + td(24), base + td(9)]
        dates = []
        for d in days:
            dates.append([d + td(hours=1.5), d + td(hours=3), d + td(hours=6)])
        for i, date_lst in enumerate(dates):
            for date in date_lst:
                ScheduleOption.objects.create(appointment=appointments[i], date=date)

