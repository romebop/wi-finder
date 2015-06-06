from flask import Flask, url_for, render_template, request
import yelp_scrape
from wifi_scraper import scrape_for_wifi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

    new_results = {}
    for key, value in yelp_results.items():
        if scrape_for_wifi.has_wifi(value[0]) == "Yes":
            new_results[key] = value

    return str(new_results)

if __name__ == '__main__':
    app.run(debug=True)
