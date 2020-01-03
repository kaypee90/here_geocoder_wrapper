heregeocoder - Python wrapper for Here.com Geocoder API!
---------------------------------------------------------

The is a python wrapper built around here.com geocoder rest api.

Requirements
------------

* **Python**:  3.6, 3.7, 3.8


Installation
------------

Install using pip:

.. code-block:: sh

    pip install heregeocoder

Usage
-----

Provide the api key you genereated on https://www.here.com/ in the GeocoderApi Constructor at the point of initialization. 
Then pass your search text in the search methode of the GeocoderApi object to receive a response object

.. code-block:: python

    from heregeocoder import GeocoderApi

	geocoder = GeocoderApi(<api_key>)
	response = geocoder.search(<search_text>)
	print(response.json())
