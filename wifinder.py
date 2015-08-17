from flask import Flask, url_for, render_template, request, send_from_directory
import yelp_scrape
import request_scrape
from itertools import islice
import json
import os

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', stuff=[])

@app.route('/wifi')
def wifi_results():
    latitude = request.args.get('latitude', '')
    longitude = request.args.get('longitude', '')
    address = request.args.get('address', '')

    if latitude != '' and longitude != '':
        yelp_results = yelp_scrape.get_yelp_coord(latitude, longitude)
    elif address != '':
        yelp_results = yelp_scrape.get_yelp_address(address)
    else:
        return "SOMETHING WENT WRONG"

    new_results = []
    print(yelp_results)
    for key, value in yelp_results.iteritems():
        if request_scrape.has_wifi(value[0]) == "Yes":
            item = {}
            item['url'] = value[0]
            item['name'] = value[1]
            item['latitude'] = key[0]
            item['longitude'] = key[1]
            new_results.append(item)
            if len(new_results) == 10:
                break

    return render_template('index.html', stuff=json.dumps(new_results));

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
