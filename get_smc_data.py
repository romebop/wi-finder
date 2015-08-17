'''
Get data from smcgov.org
'''

import json
import requests
import pprint

def get_data():
    # Get data
    r = requests.get('https://data.smcgov.org/api/views/4uz3-p92v/rows.json?accessType=DOWNLOAD')
    data = r.json()
    # Extract column names
    columns = [ thing['name'] for thing in data['meta']['view']['columns'] ]
    results = []
    for hotspot in data['data']:
        hotspot_dict = dict(zip(columns, hotspot))
        results.append(hotspot_dict)
    return results

if __name__ == '__main__':
    wifi_data = get_data()
    pprint.pprint(wifi_data)
