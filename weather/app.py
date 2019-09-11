import json
import requests
import traceback

from bs4 import BeautifulSoup

from utils import send_requests, get_geo_code

AUTHOR = {
    "name": "NIHAL RAI",
    "github": "https://github.com/nihalrai"
}


class APP:
    def __init__(self, place, date, forecast):
        self.date      = date
        self.place     = place
        self.forecast  = forecast
        
    def build_url(self, geocode):
        API_KEY = 'd522aa97197fd864d36b418f39ebb323'
        base_url = 'https://api.weather.com/v2/turbo/'
        
        forecastmethod = 'vt1dailyForecast'

        if self.forecast != 'daily':
            forecastmethod = 'vt1observation'
        
        url = base_url + forecastmethod + '?apiKey=' + API_KEY +  '&format=json&geocode=' + geocode[0] + '%2C' + geocode[1] + '&language=en-IN&units=m'
        
        return url

    def get_info(self):
        try:
            # Send request to base url with weather code and return info. 
            geocode = get_geo_code(self.place)

            if not geocode or len(geocode) != 2:
                return {}
            
            data = send_requests(self.build_url(geocode))

            if not data:
                return {}
            
            data = json.loads(data.text)
            
            if 'vt1dailyForecast' in data:
                key = 'vt1dailyForecast'
            elif 'vt1observation' in data:
                key = 'vt1observation'
            else:
                return {}

            return data[key]

        except:
            traceback.print_exc()
            return {}


    def run(self):
        """
        Method run is used for starting the crawl process and get the data
        from the same
        """
        
        try:
            result = self.get_info()
            
            if not result:
                return {}
            
            return result

        except:
            traceback.print_exc()
            return result
