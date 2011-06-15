#!/usr/bin/env python
import os
import sys

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
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
        
    )

from django.test.simple import run_tests


def runtests(*test_args):
    if not test_args:
        test_args = ['debug_toolbar_htmltidy']
    parent = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        #"..",
    )
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=2, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
