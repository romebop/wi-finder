import requests
from requests_oauthlib import OAuth1
import json
import pprint



latitude = 37.58975467000005
longitide = -122.31838430299996

# return unique list of restaurant names and urls
def get_yelp(latitude, longitide):
	search_terms = ["restaurants", "cafe", "coffee", "business"]
	#for i in range(0, len(search_terms)):
	query = {'term': search_terms[0], 'll':str(latitude) + ',' + str(longitide), 'sort':'1', 'limit':20}
	r = requests.get("http://api.yelp.com/v2/search/", params=query, auth = auth)
	return r.json()

a = get_yelp(latitude, longitide)
# dictionary structure - {(latitude, longitude): (url, name)}
def output(yelp_json):
	outDict = {}
	for business in yelp_json["businesses"]:
		if business["is_closed"] == False:
			outDict[(business["location"]["coordinate"]["latitude"], business["location"]["coordinate"]["longitude"])] = (business["url"], business["name"])
	return outDict

out = output(a)
print len(out)

"""
pprint.pprint(a["businesses"][0]["location"]["coordinate"]["latitude"]) #latitide
pprint.pprint(a["businesses"][0]["location"]["coordinate"]["longitude"]) #longitude
pprint.pprint(a["businesses"][0]["url"])
pprint.pprint(a["businesses"][0]["is_closed"]) #open or closed
pprint.pprint(a["businesses"][0]["name"]) #name
"""