import grequests
from requests_oauthlib import OAuth1
import pprint

# CONSTANTS
YELP_AUTH = OAuth1('PL4B79wNrtpTta7-V-PZTg', 'El_EkBcQyCNCpeaj6Y1yQPeUHIA', 'PeLWALWDy_zWzgMAVgp9_zQzwg-PdJJn', '6UtP4kEHB9D6u0HyOhy1y_gNxso')
YELP_BASE_URL = 'http://api.yelp.com/v2/search/'
SEARCH_TERMS = ["wifi"]


# dictionary structure - {url: {latitude, longitude, name, url}}
def _parse_output_from_yelp(yelp_json):
    result = {}
    if 'businesses' not in yelp_json:
        return {}
    for business in yelp_json["businesses"]:
        if business["is_closed"] == False:
            business_result = {}
            business_result['latitude'] = business["location"]["coordinate"]["latitude"]
            business_result['longitude'] = business["location"]["coordinate"]["longitude"]
            business_result['name'] = business["name"]
            business_result['url'] = business["url"]
            result[business['url']] = business_result
    return result

def get_yelp_results_by_address(address):
    result_dict = {}
    request_list = (grequests.get(YELP_BASE_URL, params={'term': term, 'location':address, 'sort':'1', 'limit':20}, auth=YELP_AUTH) for term in SEARCH_TERMS)

    for response in grequests.map(request_list):
        if response.status_code != 200:
            print "ERROR: Got {status_code} for url: {url}".format(status_code=response.status_code, url=response.url)
        else:
            print "Request for {0} took {1}".format(response.url, response.elapsed)
            result_for_term = _parse_output_from_yelp(response.json())
            result_dict.update(result_for_term)
    return result_dict

# return unique list of restaurant names and urls
def get_yelp_results_by_coord(latitude, longitude):
    result_dict = {}
    request_list = (grequests.get(YELP_BASE_URL, params={'term': term, 'll':'{latitude},{longitude}'.format(latitude=latitude,longitude=longitude), 'sort':'1', 'limit':20}, auth=YELP_AUTH) for term in SEARCH_TERMS)

    for response in grequests.map(request_list):
        if response.status_code != 200:
            print "ERROR: Got {status_code} for url: {url}".format(status_code=response.status_code, url=response.url)
        else:
            print "Request for {0} took {1}".format(response.url, response.elapsed)
            result_for_term = _parse_output_from_yelp(response.json())
            result_dict.update(result_for_term)
    return result_dict

if __name__ == '__main__':
    # Test data
    latitude = 37.58975467000005
    longitude = -122.31838430299996
    #address = "2128 Oxford St, Berkeley"

    a = get_yelp_results_by_coord(latitude, longitude)
    #a = get_yelp_results_by_address(address)
    pprint.pprint(a)
    print len(a)


