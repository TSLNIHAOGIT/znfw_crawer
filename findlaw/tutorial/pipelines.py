# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.utils.project import get_project_settings

class TutorialPipeline(object):

    def __init__(self):
        self.settings = get_project_settings()
        self.items = []



        # connection = pymongo.MongoClient(host=self.settings['MONGO_HOST'], port=self.settings['MONGO_PORT'])
        # self.db = connection[self.settings['MONGO_DB']]
        # 链接数据库
        self.client = pymongo.MongoClient(host=self.settings['MONGO_HOST'], port=self.settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.spider.authenticate(self.settings['MONGO_USERNAME'], self.settings['MONGO_PASSWORD'])

        self.db = self.client[self.settings['MONGO_DB']]  # 获得数据库的句柄
        # self.db.authenticate(self.settings['MONGO_USERNAME'], self.settings['MONGO_PASSWORD'],)

        # self.coll = self.db[self.settings['MONGO_COLL']]  # 获得collection的句柄
        self.collectionRecr = self.db['crawer_law_new']#**********

    def process_item(self, items, spider):
        # self.items.append(items)
        # if len(self.items)>5:
        #     print(self.items)
        #     self.items = []
        print('item***********:\n',items)
        # postItem = dict(ite m)  # 把item转化成字典形式
        # self.collectionRecr.insert(items)
        # self.coll.insert(item)  # 向数据库插入一条记录

        return items  # 会在控制台输出原item数据，可以选择不写
