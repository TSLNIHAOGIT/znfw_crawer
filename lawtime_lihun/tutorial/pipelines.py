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
        self.items_list = []
        self.items_count=0



        # connection = pymongo.MongoClient(host=self.settings['MONGO_HOST'], port=self.settings['MONGO_PORT'])
        # self.db = connection[self.settings['MONGO_DB']]
        # 链接数据库
        self.client = pymongo.MongoClient(host=self.settings['MONGO_HOST'], port=self.settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.spider.authenticate(self.settings['MONGO_USERNAME'], self.settings['MONGO_PASSWORD'])

        self.db = self.client[self.settings['MONGO_DB']]  # 获得数据库的句柄
        # self.db.authenticate(self.settings['MONGO_USERNAME'], self.settings['MONGO_PASSWORD'],)

        # self.coll = self.db[self.settings['MONGO_COLL']]  # 获得collection的句柄
        self.collectionRecr = self.db['crawer_law_more']#**********

    def process_item(self, items, spider):
        self.items_count=self.items_count+1
        # self.items.append(items)
        # if len(self.items)>5:
        #     print(self.items)
        #     self.items = []
        # print('字典长度为：',len(items['title']))
        # if len(items['title'])==0:
        print('%sitem***********:\n' %(self.items_count), items)
            # print('有问题')
        # else:
        #     print('item***********:\n',items)
        # postItem = dict(ite m)  # 把item转化成字典形式
        # self.collectionRecr.insert(items)# 向数据库插入一条记录

        return items  # 会在控制台输出原item数据，可以选择不写


    def process_item_2(self, items, spider):
        self.items_count=self.items_count+1
        self.items_list.append(items)
        if self.items_count%100==0:
            self.collectionRecr.insert(self.items_list)  # 向数据库插入一条记录
            self.items_list = []
        print('%sitem***********:\n' %(self.items_count), items)
        return items  # 会在控制台输出原