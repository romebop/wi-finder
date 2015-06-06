import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from wifi_scraper.items import *

class WifiSpider(scrapy.Spider):

    name = "wifispider"
    #allowed_domains = ["yelp.com"]
    start_urls = [""]

    def parse(self, response):
        item = WifiScraperItem()
        item['short_def_list'] = response.xpath("//div[contains(@class, 'short-def-list')]").extract()
        #print("it's the spider")

        with open('results.txt', 'w') as f:
            f.write(str(item['short_def_list'][0]))
        #return item