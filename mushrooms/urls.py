from django.conf.urls.defaults import patterns, include, url
from mushrooms.views import hello, current_datetime,my_view,field,market,mushroomBook
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
                       url(r'^hello/$', hello),
                       url(r'^time/$', current_datetime),
                       url(r'^html/$', my_view),
                       url(r'^field/$', field),
                       url(r'^market/$', market),
                       url(r'^mushroomBook/$', mushroomBook),
                       
)
from mushrooms import settings
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root':     settings.MEDIA_ROOT}),
                            )