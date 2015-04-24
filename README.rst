django-simple-gmap
==================
Simple Google Maps Integration For Django

Install
=======
``pip install django-simple-gmap``

Usage
=====
Setting things up:

- Add ``simple_gmap`` to ``INSTALLED_APPS``
- Load the django-simple-gmap template tags in your template ``{% load simple_gmap_tags %}``
- Add ``{% gmap_init 13.940823 121.163281 %}`` in your HTML head section
- Add an HTML input element with an id ``gmap-text-input``
- Add an HTML div element with an id ``gmap-canvas-object``

Example Template
================
::

    {% load simple_gmap_tags %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta http-equiv="content-type" content="text/html; charset=utf-8">
      <title>Django Simple GMap Test</title>
      {% gmap_init 13.940823 121.163281 %}
    </head>
    <body>
      <div>
        <input id="gmap-text-input" type="text" placeholder="" value="">
      </div>
      <div>&nbsp;</div>
      <div>
        <div id="gmap-canvas-object"></div>
      </div>
    </body>
    </html>