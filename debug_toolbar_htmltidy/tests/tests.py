from debug_toolbar.toolbar.loader import DebugToolbar
from debug_toolbar_htmltidy.panels import HTMLTidyDebugPanel

from django.conf import settings
from django.test import TestCase

from dingus import Dingus

import os


class Settings(object):
    """Allows you to define settings that are required
    for this function to work"""

    NotDefined = object()

    def __init__(self, **overrides):
        self.overrides = overrides
        self._orig = {}

    def __enter__(self):
        for k, v in self.overrides.iteritems():
            self._orig[k] = getattr(settings, k, self.NotDefined)
            setattr(settings, k, v)

    def __exit__(self, exc_type, exc_value, traceback):
        for k, v in self._orig.iteritems():
            if v is self.NotDefined:
                delattr(settings, k)
            else:
                setattr(settings, k, v)


class BaseTestCase(TestCase):
    def setUp(self):
        settings.DEBUG = True
        settings.DEBUG_TOOLBAR_PANELS = self.panels_list
        settings.TEMPLATE_DIRS = (
                os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    'templates/'),
                )
        settings.MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        )

        request = Dingus('request')
        toolbar = DebugToolbar(request)
        toolbar.load_panels()

        self.request = request
        self.toolbar = toolbar

    def panel(self):
        for panel in self.toolbar.panels:
            if panel.__class__ == self.panel_class:
                return panel

        return None


class ViewBasedTestCase(BaseTestCase):
    urls = 'debug_toolbar_htmltidy.tests.urls'
    panel_class = None
    view_url = None

    def fetch_view(self):
        # basic case
        with Settings(DEBUG=True):
            resp = self.client.get(self.view_url)

        return resp


class HTMLValidationDebugPanelTestCase(ViewBasedTestCase):
    urls = 'debug_toolbar_htmltidy.tests.urls'
    panel_class = HTMLTidyDebugPanel
    panels_list = (
    'debug_toolbar_htmltidy.panels.HTMLTidyDebugPanel',)

    view_url = '/'

    def panel(self):
        panel = super(self.__class__, self).panel()

        self.assertEquals(panel.errors_count, 0)
        self.assertEquals(panel.warns_count, 0)

        return panel

    def test_validator_counters(self):
        panel = self.panel()
        resp = self.fetch_view()

        # process response by hand
        panel.process_response(self.request, resp)

        self.assertEqual(panel.errors_count, 1)
        self.assertEqual(panel.warns_count, 6)

    def test_apperance_builder(self):
        panel = self.panel()
        resp = self.fetch_view()

        # process response by hand
        panel.process_response(self.request, resp)
        document, errors = panel.log_data

        builded_errors = panel.appearance(errors)

        self.assertEqual("".join(builded_errors).count('validation-error'), 2)
        self.assertEqual(len(builded_errors), 8)

    def test_media(self):
        resp = self.fetch_view()
        panel = self.panel()
        panel.process_response(self.request, resp)
        html = panel.content()

        self.assertTrue('/__htmltidy_debug__/m/js/htmltidypanel.min.js' \
                        in html)
        self.assertTrue('/__htmltidy_debug__/m/css/htmltidypanel.min.css' \
                        in html)
