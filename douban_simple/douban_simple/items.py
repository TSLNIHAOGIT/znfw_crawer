# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    movie_name = scrapy.Field() #电影名称
    movie_star = scrapy.Field() #电影评分
    movie_url = scrapy.Field() #电影链接

