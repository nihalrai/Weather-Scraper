import json
import requests
import traceback


def send_requests(url):
    try:
    
        # Send request to passed url and return response if successful
        response = requests.get(url, allow_redirects=True, timeout=10)
        
        if response and response.status_code in range(200, 300):
            return response
        
        return None
    except:
        traceback.print_exc()
        return None

def get_geo_code(place):
    response = send_requests('https://geocode.xyz/{}?json=1'.format(place))
    latt, longt = 0, 0
    
    if not response:
        return None
    
    try:
        json_resp = json.loads(response.text)
        if 'latt' in json_resp:
            latt = str(round(float(json_resp['latt']), 2))
        
        if 'longt' in json_resp:
            longt = str(round(float(json_resp['longt']), 2))
        
        if longt == 0 or latt == 0:
            return 0
        return [latt, longt]

    except:
        traceback.print_exc()
        return None