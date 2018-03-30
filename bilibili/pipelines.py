# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.exceptions import DropItem
import settings

class BilibiliPipeline(object):
    collection_name = 'bili_user'
    def __init__(self,mongo_host,mongo_port,mongo_db):
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_host=crawler.settings.get('MONGO_HOST')
            mongo_port=crawler.settings.get('MONGO_PORT')
            mongo_db=crawler.settings.get('DB_NAME')
        )

    def open_spider(self,spider):
        self.client = MongoClient(self.mongo_host,self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()


    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item
