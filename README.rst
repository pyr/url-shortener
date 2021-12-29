Gurl-shortener: demo URL shortening service in python
=====================================================

A demo application for a very simple URL shortening service

The app relies on:

- flask_: A python micro web framework
- bootstrap_: A CSS & JS framework


Installing
----------

Pip::

    pip install url_shortener

Pypi:

    https://pypi.python.org/pypi/url_shortener

Manual::

    python setup.py install

Configuration
-------------

You can either modify the ``config.py`` file or provide environment
variables to configure ``url_shortener``. The following environment
variables can be tweaked:

- ``REDIS_HOST``: Address at which the redis server lives, defaults to ``127.0.0.1``.
- ``REDIS_PORT``: Port on which to contact redis, defaults to ``6379``.
- ``URL_PREFIX``: URL scheme for your short url host
- ``LISTEN_HOST``: Address to bind to for the short url service
- ``LISTEN_PORT``: Port to bind to

Usage
-----

The service can simply be started by invoking: ``url-shortener``, alternately deployments can
be done via Docker:

::

  docker run --rm -p 5000:5000 url-shortener:latest

.. _flask: http://flask.pocoo.org
.. _bootstrap: http://twitter.github.io/bootstrap
.. _gunicorn: http://gunicorn.org
