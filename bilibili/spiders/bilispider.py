import scrapy
from scrapy.spider import CrawlSpider
from scrapy import Selector
from scrapy.loader import ItemLoader
from items import BilibiliItem

class BiliSpider(CrawlSpider):

    name = 'bilibili'
    allow_domain = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking#!/all/119/0/30/']
    rules = ()

    def parse_item(self,response):
        video_links = response.xpath(".//*[class='content clearfix']/a/@href")
        for v_link in video_links:
            yield scrapy.Request(response.urljoin(v_link),callback=self.video)

    def video(self,response):
        user_links = Selector(response).re(r'href="(//space.bilibili.com/\d+)"')
        for u_link in user_links:
            yield scrapy.Request(u_link,callback=self.user)

    def user(self,response):
        item = ItemLoader(item=BilibiliItem(),response=response)
        item.add_xpath('name', '//span[@id="h-name"]/text')
        item.add_xpath('gender', '//span[@id="h-gender"]@class')
        item.add_xpath('is_vip', 'xpath')
        yield item

    next_page = Selector(response).
