from django.contrib import admin
from .models import Appointment, Participant, ScheduleOption, AcceptedOption


class ScheduleOptionInline(admin.StackedInline):
    model = ScheduleOption


class AcceptedOptionInline(admin.StackedInline):
    model = AcceptedOption


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_display = ['text', 'owner', 'invited']
    filter_vertical = ['participants']
    inlines = [ScheduleOptionInline]

    def invited(self, obj):
        return ', '.join([p.name for p in obj.participants.all()])


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Appointment, AppointmentAdmin)

