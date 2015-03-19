from django.conf.urls import patterns, url, include

from .api import *

appointment_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', AppointmentDetail.as_view(),
        name='appointment-detail'),
    url(r'^$', AppointmentList.as_view(), name='api-appointment-list'),
)

participant_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', ParticipantDetail.as_view(), name='api-participant'),
    #url(r'^/(?P<pk>\d+)/accepted/(?P<appointment>\d+)$',
        #ParticipantDetail.as_view(), name='api-accepted-by'),
)

urlpatterns = patterns('',
    url(r'^accepted/(?P<appointment>\d+)/(?P<participant>\d+)$',
        AcceptedList.as_view(), name='accepted-list'),
    url(r'^accepted/(?P<appointment>\d+)/(?P<participant>\d+)/update$',
        update_accepted_view, name='accepted-update'),
    url(r'^appointments', include(appointment_urls)),
    url(r'^participants', include(participant_urls)),
)
