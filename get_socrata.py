from flask import Flask, url_for, render_template
from sodapy import Socrata
import pprint
import json

app = Flask(__name__)

client = Socrata("data.smcgov.org", "FakeAppToken", username="team7", password="2fortheBASS")

#client.get('/resource/nimj-3ivp.json')

@app.route("/")
def index():
	return client.get("/resource/4uz3-p92v.json")

if __name__ == "__main__":
	app.run()