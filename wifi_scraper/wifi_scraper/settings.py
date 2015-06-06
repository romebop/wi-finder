# -*- coding: utf-8 -*-

# Scrapy settings for wifi_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wifi_scraper'

SPIDER_MODULES = ['wifi_scraper.spiders']
NEWSPIDER_MODULE = 'wifi_scraper.spiders'

#ITEM_PIPELINES = {
#	'wifi_scraper.pipelines.WifiScraperPipeline': 0,
#}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wifi_scraper (+http://www.yourdomain.com)'
