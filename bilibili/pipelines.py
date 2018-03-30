# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from . import settings

class BilibiliPipeline(object):
    def __init__(self):
        self.client = MongoClient(settings.MONGO_HOST,settings.MONGO_PORT)
        self.db = self.client[settings.DB_NAME]
        self.sheet = self.db[settings.SHEET]

    def process_item(self, item, spider):
        return item
