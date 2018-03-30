# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    genter = scrapy.Field()
    vip = scrapy.Field()
    age = scrapy.Field()
    register_date = scrapy.Field()
