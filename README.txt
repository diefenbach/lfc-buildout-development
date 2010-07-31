What is it?
===========

This is the 1.0 branch development buildout script for LFC. 

It will create a complete developement environment for LFC. 

LFC is a CMS based on Python, Django and jQuery.

How to use it?
==============

1. Check it out from bitbucket
    
    $ hg clone https://bitbucket.org/diefenbach/lfc-buildout-development-1.0

2. Change to the directory

    $ cd lfc-buildout-development-1.0
    
3. Bootstrap buildout

    $ python bootstrap 
    
4. Run buildout

    $ bin/buildout -v
    
5. Enter your database settings into lfc_project/settings.py

6. Sync your database

    $ bin/django syncdb
    
7. Initialize LFS

    $ bin/django lfc_init

8. Start server

    $ bin/django runserver
    
9. Browse to LFS

    http://localhost:8000
    
More Information
================

* `Official page <http://www.lfcproject.com/>`_
* `Documentation on PyPI <http://packages.python.org/django-lfc/index.html>`_
* `Releases on PyPI <http://pypi.python.org/pypi/django-lfc>`_
* `Source code on bitbucket.org <http://bitbucket.org/diefenbach/django-lfc>`_
* `Google Group <http://groups.google.com/group/django-lfc>`_
* `lfsproject on Twitter <http://twitter.com/lfcproject>`_
* `IRC <irc://irc.freenode.net/django-lfc>`_