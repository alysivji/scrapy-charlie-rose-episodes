# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CharlieRoseItem(scrapy.Item):
    '''
    Defining the storage containers for the data we
    plan to scrape
    '''

    date = scrapy.Field()
    guest = scrapy.Field()
    url = scrapy.Field()
    seen = scrapy.Field()
