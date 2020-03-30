
======================
Leonardo Sentry Module
======================

Provide end-user friendly 500 Error handler for Leonardo Sites

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo_module_sentry

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["sentry"]

Add ``leonardo_module_sentry`` to APPS list, in the ``local_settings.py``::

    APPS = [
    	...
        'leonardo_module_sentry'
    	...
    ]


Add ``SENTRY_DSN`` into your ``local_settings.py``::

SENTRY_DSN = 'http://public:secret@example.com/1'

