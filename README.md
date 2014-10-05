pyfatsecret
===========

This library provides a lightweight python wrapper for the Fatsecret API with the goal of making it easier to visualize
the data retrieved from the API. To that end, this library will usually return lists of identical elements for ease of
plotting, discarding extra header fields that the Fatsecret API otherwise includes. All API calls return a either a
single or list of JSON dictionaries.

Fatsecret supports both delegated and public calls. Only through delegated calls can you access Fatsecret user
profile data.

Install
-----

Via Pip

    $ pip install fatsecret
    
Via Easy Install

    $ easy_install fatsecret

Config
------

Register for a developer account to get a consumer key and secret key from http://platform.fatsecret.com/api/

Usage
-----

    from fatsecret import Fatsecret
    
    fs = Fatsecret(consumer_key, consumer_secret)
    
    foods = fs.foods_search("Taco")

Refer to the [documentation](http://pyfatsecret.readthedocs.org/en/latest/) for further examples and detail

