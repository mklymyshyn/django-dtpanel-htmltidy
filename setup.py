from setuptools import setup, find_packages

setup(
    name='django-dtpanel-htmltidy',
    version='0.1.1',
    description='Custom panel form Django Debug Toolbar which display HTML Validation errors and warnings',
    long_description=open('README.markdown').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Max Klymyshyn',
    author_email='klymyshyn@gmail.com',
    url='https://github.com/joymax/django-dtpanel-htmltidy',
    download_url='https://github.com/joymax/django-dtpanel-htmltidy/downloads',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    tests_require=[
        'django',
        'django-debug-toolbar',
        'dingus',
    ],
    install_requires=[
       'pytidylib',
    ],
    test_suite='debug_toolbar_htmltidy.runtests.runtests',
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
