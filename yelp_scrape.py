import requests
from requests_oauthlib import OAuth1
import json
import pprint

latitude = 37.58975467000005
longitude = -122.31838430299996
address = "2128 Oxford St, Berkeley"
auth = OAuth1('PL4B79wNrtpTta7-V-PZTg', 'El_EkBcQyCNCpeaj6Y1yQPeUHIA', 'PeLWALWDy_zWzgMAVgp9_zQzwg-PdJJn', '6UtP4kEHB9D6u0HyOhy1y_gNxso')

# dictionary structure - {(latitude, longitude): (url, name)}
def output(yelp_json):
    outDict = {}
    if 'businesses' not in yelp_json:
        return {}
    for business in yelp_json["businesses"]:
        if business["is_closed"] == False:
            outDict[(business["location"]["coordinate"]["latitude"], business["location"]["coordinate"]["longitude"])] = (business["url"], business["name"])
    return outDict

def get_yelp_address(address):
    search_terms = ["cafe", "coffee", "restaurants", "bar"]
    finalOut = {}
    for term in search_terms:
        query = {'term': term, 'location':address, 'sort':'1', 'limit':20}
        r = requests.get("http://api.yelp.com/v2/search/", params=query, auth = auth)
        out = output(r.json())
        finalOut.update(out)
    return finalOut

# return unique list of restaurant names and urls
def get_yelp_coord(latitude, longitide):
    search_terms = ["restaurants", "cafe", "coffee", "bar"]
    finalOut = {}
    for term in search_terms:
        query = {'term': term, 'll':str(latitude) + ',' + str(longitide), 'sort':'1', 'limit':20}
        r = requests.get("http://api.yelp.com/v2/search/", params=query, auth = auth)
        out = output(r.json())
        finalOut.update(out)
    return finalOut

if __name__ == '__main__':
    #a = get_yelp_coord(latitude, longitide)
    a = get_yelp_address(address)
    pprint.pprint(a)
    print len(a)


