import scrapy

class BiliSpider(scrapy.Spider):

    name = 'bilibili'
    allow_domain = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking#!/all/119/0/30/']
