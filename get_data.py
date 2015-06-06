import json
import requests

r = requests.get('https://data.smcgov.org/api/views/4uz3-p92v/rows.json?accessType=DOWNLOAD')

data = r.json()
first_wifi_hotspot = data['data'][0]

print first_wifi_hotspot
