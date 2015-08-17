import requests
from requests_oauthlib import OAuth1
import pprint

# CONSTANTS
YELP_AUTH = OAuth1('PL4B79wNrtpTta7-V-PZTg', 'El_EkBcQyCNCpeaj6Y1yQPeUHIA', 'PeLWALWDy_zWzgMAVgp9_zQzwg-PdJJn', '6UtP4kEHB9D6u0HyOhy1y_gNxso')
YELP_BASE_URL = 'http://api.yelp.com/v2/search/'


# dictionary structure - {(latitude, longitude): (url, name)}
def _parse_output_from_yelp(yelp_json):
    outDict = {}
    if 'businesses' not in yelp_json:
        return {}
    for business in yelp_json["businesses"]:
        if business["is_closed"] == False:
            outDict[(business["location"]["coordinate"]["latitude"], business["location"]["coordinate"]["longitude"])] = (business["url"], business["name"])
    return outDict

def get_yelp_results_by_address(address):
    search_terms = ["cafe", "coffee", "restaurants", "bar"]
    result_dict = {}
    for term in search_terms:
        query = {'term': term, 'location':address, 'sort':'1', 'limit':20}
        r = requests.get(YELP_BASE_URL, params=query, auth=YELP_AUTH)
        result_for_term = _parse_output_from_yelp(r.json())
        result_dict.update(result_for_term)
    return result_dict

# return unique list of restaurant names and urls
def get_yelp_results_by_coord(latitude, longitide):
    search_terms = ["restaurants", "cafe", "coffee", "bar"]
    result_dict = {}
    for term in search_terms:
        query = {'term': term, 'll':'{latitude},{longitude}'.format(latitude=latitude,longitide=longitude), 'sort':'1', 'limit':20}
        r = requests.get(YELP_BASE_URL, params=query, auth=YELP_AUTH)
        result_for_term = _parse_output_from_yelp(r.json())
        result_dict.update(result_for_term)
    return result_dict

if __name__ == '__main__':
    # Test data
    latitude = 37.58975467000005
    longitude = -122.31838430299996
    address = "2128 Oxford St, Berkeley"

    #a = get_yelp_results_by_coord(latitude, longitide)
    a = get_yelp_results_by_address(address)
    pprint.pprint(a)
    print len(a)


