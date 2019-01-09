# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
#
#
# class DoubanItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


import scrapy


class DoubanBookItem(scrapy.Item):
    name = scrapy.Field()  # 书名
    price = scrapy.Field()  # 价格
    edition_year = scrapy.Field()  # 出版年份
    publisher = scrapy.Field()  # 出版社
    ratings = scrapy.Field()  # 评分


class DoubanMailItem(scrapy.Item):
    sender_time = scrapy.Field()     # 发送时间
    sender_from = scrapy.Field()     # 发送人
    url = scrapy.Field()             # 豆邮详细地址
    title = scrapy.Field()           # 豆邮标题