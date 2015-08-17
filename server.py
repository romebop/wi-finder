from flask import Flask, url_for, render_template, request, send_from_directory
import yelp_scrape
import request_scrape
from itertools import islice
import json
import os
import threading

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

app = Flask(__name__)

new_results = []

@app.route('/')
def index():
    return render_template('index.html', stuff=[])

def worker(key, value):
    if request_scrape.has_wifi(value[0]) == "Yes":
        item = {}
        item['url'] = value[0]
        item['name'] = value[1]
        item['latitude'] = key[0]
        item['longitude'] = key[1]
        new_results.append(item)
        return item

@app.route('/wifi')
def wifi_results():
    latitude = request.args.get('latitude', '')
    longitude = request.args.get('longitude', '')
    address = request.args.get('address', '')

    if latitude != '' and longitude != '':
        yelp_results = yelp_scrape.get_yelp_results_by_coord(latitude, longitude)
    elif address != '':
        yelp_results = yelp_scrape.get_yelp_results_by_address(address)
    else:
        return "SOMETHING WENT WRONG"

    try:
        threads = []
        for key, value in take(10, yelp_results.iteritems()):
            t = threading.Thread(target = worker, args=(key,value,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        return render_template('index.html', stuff=json.dumps(new_results));
    except Exception, e:
        print e

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
