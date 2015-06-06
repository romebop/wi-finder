from bs4 import BeautifulSoup
import os
import subprocess

def has_wifi(url):
        FNULL = open(os.devnull, 'w')
        subprocess.call("scrapy parse {url} --spider=wifispider".format(url=url).split(), stdout=FNULL, stderr=subprocess.STDOUT)

        current_dir = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(current_dir, 'results.txt'), 'r') as f:
                stuff = f.readlines()
                one_liner = "".join(stuff)
        soup = BeautifulSoup(one_liner)
        dls = soup.find_all('dl')
        wifi = "N/A"
        for dl in dls:
                temp_field = dl.dt.string.strip()
                temp_val = dl.dd.string.strip()
                if temp_field == "Wi-Fi":
                        wifi = "No" 
                        if temp_val != "No":
                                wifi = "Yes"
        return wifi

if __name__ == '__main__':
        print has_wifi('http://www.yelp.com/biz/cafe-milan-playa-del-rey')
