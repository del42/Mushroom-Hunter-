from django.conf.urls.defaults import patterns, include, url
from mushrooms.views import hello, current_datetime,my_view


urlpatterns = patterns('',
                       url(r'^hello/$', hello),
                       url(r'^time/$', current_datetime),
                       url(r'^html/$', my_view),
)
