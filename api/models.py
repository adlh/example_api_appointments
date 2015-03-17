from django.db import models
from collections import Counter, namedtuple

BestOption = namedtuple('BestOption', 'date count')
OptionOverview = namedtuple('OptionOverview', 'date participants')

class Participant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    owner = models.ForeignKey(Participant, related_name='appointments')
    text = models.TextField(blank=True, null=True)
    participants = models.ManyToManyField(Participant)

    def __str__(self):
        return '%s [%s]' % (self.text[:25], self.owner)

    @property
    def best_options(self):
        """ Return all accepted options ordered by most accepted """
        accepted = AcceptedOption.objects.filter(option__appointment=self)
        c = Counter([a.option.date_str for a in accepted])
        return [BestOption(date, cnt) for date, cnt in c.most_common()]

    @property
    def option_overview(self):
        return [OptionOverview(op.date_str, ', '.join(
            [a.participant.name for a in op.acceptedoption_set.all()]))
            for op in self.options.all()]


class ScheduleOption(models.Model):
    date = models.DateTimeField()
    appointment = models.ForeignKey(Appointment, related_name='options')

    def __str__(self):
        return self.date.strftime('%A, %m %b %Y - %H:%M')

    @property
    def date_str(self):
        return self.date.strftime('%A, %m %b %Y - %H:%M')


class AcceptedOption(models.Model):
    option = models.ForeignKey(ScheduleOption)
    participant = models.ForeignKey(Participant,
            related_name='possible_options')

    class Meta:
        unique_together = ('option', 'participant')

    def __str__(self):
        return '%s accepts %s' % (self.participant, self.option)



