
HTML Tidy/Validator Panel for Django Debug Toolbar
========

The Django Debug Toolbar is a configurable set of panels that display various
debug information about the current request/response and when clicked, display
more details about the panel's content.

HTML Tidy or HTML Validatory is custom panel for Django Debug Panel which
validate your HTML and display warning and errors as panel.

Panel code based on PyTidyLib

Installation & Configuration
-----------------

1. Please, make sure that you have `tidy` librart installed:

  * `libtidy-dev` for Ubuntu
  * `tidy` for Mac Ports (Mac OS X)

1. Install and configure `django-debug-toolbar` app

1. Add the `debug_toolbar_htmltidy` directory to your Python path.

1. Add `debug_toolbar_htmltidy` to your `INSTALLED_APPS` in `settings.py` file:
***
        INSTALLED_APPS += (
            'debug_toolbar_htmltidy',
        )

1. Add the following panel to your Django Debug Toolbar panels
   configuration tuple in `settings.py` file:

***
        DEBUG_TOOLBAR_PANELS = (
	    ...
	    'debug_toolbar_htmltidy.panels.HTMLTidyDebugPanel',
        )

1. Include in file which specified in `ROOT_URLCONF` setting in `settings.py`
   url to `HTMLTidyDebugPanel` media:

***
    	url(r'^', include('debug_toolbar_htmltidy.urls'))


Running the Tests
-----------------

The HTML Tidy Panel for Django Debug Toolbar includes a test suite
::

    python setup.py test


Tests result
=================

	Django	Debug Toolbar	Status
	------------------------------
	1.1.1	0.8.5			passed
	1.1.1	0.8.4			passed
	1.1.1	0.8.3			passed
	1.1.1	0.8.2			passed
	1.1.1	0.8.1			failed
	1.1.1	0.8.0			failed
	1.2		0.8.5			passed
	1.2		0.8.4			passed
	1.2		0.8.3			passed
	1.2		0.8.2			passed
	1.2		0.8.1			failed
	1.2		0.8.0			failed
	1.3		0.8.5			passed
	1.3		0.8.4			passed
	1.3		0.8.3			passed
	1.3		0.8.2			passed
	1.3		0.8.1			failed
	1.3		0.8.0			failed


TODOs and BUGS
==============
See: [issue tracker on github](https://github.com/joymax/django-dtpanel-htmltidy/issues)
