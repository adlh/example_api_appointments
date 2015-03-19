from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from pprint import pformat

import logging

logger = logging.getLogger(__name__)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^$', TemplateView.as_view(template_name='appointments.html'),
        name='appointment-list'),
    url(r'^view/(?P<pk>\d+)$', TemplateView.as_view(
        template_name='appointment-view.html'), name='appointment-view'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

