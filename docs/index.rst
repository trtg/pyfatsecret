.. pyfatsecret documentation master file, created by
   sphinx-quickstart on Fri Oct  3 09:09:41 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyfatsecret documentation
=================

This library provides a lightweight python wrapper for the Fatsecret API with the goal of making it easier to visualize
the data retrieved from the API. To that end, this library will usually return lists of identical elements for ease of
plotting, discarding extra header fields that the Fatsecret API otherwise includes. All API calls return a either a
single or list of JSON dictionaries.

Fatsecret supports both delegated and undelegated calls. Only through delegated calls can you access Fatsecret user
profile data.

Contents:

.. toctree::

    setup
    usage

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

