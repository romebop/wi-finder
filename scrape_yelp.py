'''
Get result json from yelp_api.py and start scraping yelp
'''

from bs4 import BeautifulSoup
import grequests

import time

THROTTLE = 10

def has_wifi(yelp_api_results):
    results = []
    yelp_scrape_requests = (grequests.get(url) for url in yelp_api_results)

    for response in grequests.map(yelp_scrape_requests, size=THROTTLE):
        if response.status_code != 200:
            print "ERROR: Got {status_code} for url: {url}".format(status_code=response.status_code, url=response.url)
        else:
            start = time.time()
            soup = BeautifulSoup(response.text, "html.parser")
            short_def_list = soup.find("div", {"class": "short-def-list"})
            if short_def_list is not None:
                dls = short_def_list.find_all('dl')
                # print dls

                for dl in dls:
                    temp_field = dl.dt.string.strip()
                    temp_val = dl.dd.string.strip()

                    if temp_field == "Wi-Fi" and temp_val != "No":
                        results.append(yelp_api_results[response.url])
            bs_time = time.time() - start
            print "Request for {url} took {request_time}. BeautifulSoup took {bs_time} to parse it".format(url=response.url, request_time=response.elapsed, bs_time=bs_time)

    return results

if __name__ =='__main__':
    print "GOOD"
