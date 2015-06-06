import requests
from requests_oauthlib import OAuth1
import json
import pprint


latitude = 37.58975467000005
longitide = -122.31838430299996
address = "1900 Coyote Point Drive"

# dictionary structure - {(latitude, longitude): (url, name)}
def output(yelp_json):
    outDict = {}    
    for business in yelp_json["businesses"]:
        if business["is_closed"] == False:
            outDict[(business["location"]["coordinate"]["latitude"], business["location"]["coordinate"]["longitude"])] = (business["url"], business["name"])
    return outDict

def get_yelp_address(address):
    search_terms = ["restaurants", "cafe", "coffee", "bar"]
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


