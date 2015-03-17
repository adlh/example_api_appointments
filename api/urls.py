from django.conf.urls import patterns, url, include

from .api import AppointmentDetail, AppointmentList

appointment_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', AppointmentDetail.as_view(),
        name='api-appointment-detail'),
    url(r'^$', AppointmentList.as_view(), name='api-appointment-list'),
)

urlpatterns = patterns('',
    url(r'^appointments', include(appointment_urls)),
)
