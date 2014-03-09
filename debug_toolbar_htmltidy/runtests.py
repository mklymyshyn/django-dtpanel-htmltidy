#!/usr/bin/env python
import os
import sys

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'django.contrib.admin',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',

            'debug_toolbar',
            'debug_toolbar_htmltidy',
            'debug_toolbar_htmltidy.tests',
        ],
        ROOT_URLCONF='debug_toolbar_htmltidy.tests.urls',
        MIDDLEWARE_CLASSES=[
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        ],
        TEMPLATE_DEBUG=True,
        DEBUG=True,
        SITE_ID=1,
        DEBUG_TOOLBAR_PANELS=['debug_toolbar_htmltidy.panels.HTMLTidyDebugPanel'],
    )

from django.test.utils import get_runner


def runtests(*test_args):
    if not test_args:
        test_args = ['debug_toolbar_htmltidy']
    app_dir = os.path.dirname(os.path.abspath(__file__))
    parent = os.path.join(app_dir, '..')
    sys.path.insert(0, parent)
    runner_class = get_runner(settings)
    test_runner = runner_class(pattern='*s.py', verbosity=2, interactive=True)
    failures = test_runner.run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
