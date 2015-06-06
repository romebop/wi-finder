from flask import Flask, url_for, render_template, request
import yelp_scrape


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

    return str(yelp_results)

if __name__ == '__main__':
    app.run(debug=True)
