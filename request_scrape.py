from bs4 import BeautifulSoup
import requests

def has_wifi(url):

	print("@@@ we're here: " + url)

	wifi = "N/A"

	response = requests.get(url)

	soup = BeautifulSoup(response.text)
	short_def_list = soup.find("div", {"class": "short-def-list"})
	dls = short_def_list.find_all('dl')
	# print dls

	for dl in dls:
		temp_field = dl.dt.string.strip()
		temp_val = dl.dd.string.strip()

		if temp_field == "Wi-Fi":
			wifi = "No" 
			if temp_val != "No":
				wifi = "Yes"

	return wifi