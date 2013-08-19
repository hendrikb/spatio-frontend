from django.conf.urls import patterns, include, url
from spatio_main.api import api


urlpatterns = patterns('',
    url(r'^api/', include(api.urls)),
)
