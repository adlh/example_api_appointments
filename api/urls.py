from django.conf.urls import patterns, url, include

from .api import AppointmentDetail

appointment_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', AppointmentDetail.as_view(), name='appointment-detail'),
)

urlpatterns = patterns('',
    url(r'^appointment', include(appointment_urls)),
)
