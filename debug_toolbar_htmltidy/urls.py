from django.conf.urls.defaults import url, patterns
from django.conf import settings

_PREFIX = '__htmltidy_debug__'

urlpatterns = patterns('',
    url(r'^%s/m/(.*)$' % _PREFIX, 'debug_toolbar_htmltidy.views.debug_media'),
)
