import os
from django.conf import settings
from django.views.static import serve


def debug_media(request, path):
    """View to serve media for debug_toolbar_Htmltidy"""
    root = getattr(settings, 'DEBUG_TOOLBAR_HTMLTIDY_MEDIA_ROOT', None)
    if root is None:
        parent = os.path.abspath(os.path.dirname(__file__))
        root = os.path.join(parent, 'static', 'debug_toolbar_htmltidy')
    return serve(request, path, root)
