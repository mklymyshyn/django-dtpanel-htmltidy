from django.conf.urls.defaults import patterns, url, include
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'^$', direct_to_template, {
    'template': 'htmlvalidator.html',
    }),
    url(r'^', include('debug_toolbar_htmltidy.urls'))
)
