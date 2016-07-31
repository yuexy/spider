# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TooopenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    ImageSetlink = scrapy.Field()
    Imagelink = scrapy.Field()
    NextPagelink= scrapy.Field()
    image_urls = scrapy.Field()
