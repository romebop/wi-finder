from flask import Flask, url_for, render_template, request, send_from_directory
import yelp_api
import json
import os

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
        yelp_results = yelp_api.get_yelp_results_by_coord(latitude, longitude)
    elif address != '':
        yelp_results = yelp_api.get_yelp_results_by_address(address)
    else:
        return "SOMETHING WENT WRONG"

    #print len(yelp_results)
    results = yelp_results.values()
    return render_template('index.html', stuff=json.dumps(results))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
