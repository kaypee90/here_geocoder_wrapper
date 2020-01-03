import requests

BASE_URL = "https://geocoder.ls.hereapi.com/6.2/geocode.json"

class GeocoderApi:
    """Geocoder API wrapper class """

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = BASE_URL
    
    def search(self, search_text):
        """Summary or Description of the Function

        Parameters:
        search_text (int): address being searched for

        Returns:
        object: python request library response object

       """
        response = requests.get(
            self.base_url,
            params={
                'searchtext': search_text,
                'apiKey': self.api_key
            },
            headers={'Accept': 'application/json'},
        )
        return response
    