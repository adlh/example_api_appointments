from django.db import models
from django.conf import settings
from collections import Counter, namedtuple

import pytz

BestOption = namedtuple('BestOption', 'date count')
OptionOverview = namedtuple('OptionOverview', 'id date participants')
People = namedtuple('People', 'id name email')

class Participant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def get_accepted(self, app_id):
        return self.accepted_options.filter(option__appointment__id=app_id)

    def update_accepted(self, app_id, options=[]):
        """ Options should be a list of ids of the accepted options for this
        participant. """
        available = Appointment.objects.get(pk=app_id).options.all()
        accepted = self.get_accepted(app_id)
        # Use sets with option-ids to find out which options should be
        # added/removed
        acc = set([a.option.id for a in accepted])
        up = set(options)
        # The options to add are in up but not in acc and viceversa to delete
        # Add new options
        add = up - acc
        for op_id in add:
            # get the option (it can only be one so this is safe)
            op = [op for op in available if op.id == op_id][0]
            if op:
                AcceptedOption.objects.create(participant=self, option=op)
        # ... and remove
        rm = acc - up
        for op_id in rm:
            # get the option (it can only be one so this is safe)
            a_op = [a_op for a_op in accepted if a_op.option.id == op_id][0]
            if a_op:
                a_op.delete()



class Appointment(models.Model):
    owner = models.ForeignKey(Participant, related_name='appointments')
    text = models.TextField(blank=True, null=True)
    participants = models.ManyToManyField(Participant)

    def __str__(self):
        return '%s [%s]' % (self.text[:25], self.owner)

    # Some properties to send extra infos on the serializer
    @property
    def best_options(self):
        """ Return all accepted options ordered by most accepted """
        accepted = AcceptedOption.objects.filter(option__appointment=self)
        c = Counter([a.option.date_str for a in accepted])
        return [BestOption(date, cnt) for date, cnt in c.most_common()]

    @property
    def option_overview(self):
        """ Return all available options with an overview of the people
        which marked this option as possible. """
        return [OptionOverview(op.id, op.date_str, ', '.join(
            [a.participant.name for a in op.acceptedoption_set.all()]))
            for op in self.options.all()]


class ScheduleOption(models.Model):
    date = models.DateTimeField()
    appointment = models.ForeignKey(Appointment, related_name='options')

    def __str__(self):
        local_tz = pytz.timezone(settings.TIME_ZONE)
        return self.date.replace(tzinfo=pytz.utc).astimezone(
                local_tz).strftime('%A, %d %b %Y - %H:%M')

    @property
    def date_str(self):
        return self.__str__()



class AcceptedOption(models.Model):
    option = models.ForeignKey(ScheduleOption)
    participant = models.ForeignKey(Participant,
            related_name='accepted_options')

    class Meta:
        unique_together = ('option', 'participant')

    def __str__(self):
        return '%s accepts %s' % (self.participant, self.option)



