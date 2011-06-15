from django.conf import settings

from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns, url, include


#from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'^$', direct_to_template, {
        'template': 'index.html'}),
    url(r'^', include('debug_toolbar_htmltidy.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }))
