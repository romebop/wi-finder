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

    if latitude == '' or longitude == '':
        return 'Cannot get coordinates'

    yelp_results = yelp_scrape.get_yelp(latitude, longitude)

    return str(yelp_results)

if __name__ == '__main__':
    app.run(debug=True)
