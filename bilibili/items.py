# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    gender = scrapy.Field()
    # 会员等级
    level = scrapy.Field()
    # 是否大会员
    is_vip = scrapy.Field()
    age = scrapy.Field()
    # 关注数
    follow = scrapy.Field()
    # 粉丝数
    fans = scrapy.Field()
    # 视频播放量
    video_check = scrapy.Field()
    # 阅读数
    video_view = scrapy.Field()
    # 是否认证
    is_auth = scrapy.Field()
    # 总充电人数
    elec_count = scrapy.Field()
    # 用户UID
    uid = scrapy.Field()
    register_date = scrapy.Field()
    birthay = scrapy.Field()
    location = scrapy.Field()
    # 投稿数
    contribute_num = scrapy.Field()
