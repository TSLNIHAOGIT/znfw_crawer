# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class DoubanSimplePipeline(object):
#     def process_item(self, item, spider):
#         return item
import pymysql

class DoubanPipeline(object):
    def process_item(self, item, spider):
        print  (u'数据库写入准备...')
        con = pymysql.connect('localhost','root','密码','douban',charset='utf8')
        cur = con.cursor()
        cur.execute('set names "utf8"')
        sql = "insert into movies(name,points,url) values(%s,%s,%s)"
        lis = (item['movie_name'],item['movie_star'],item['movie_url'])
        # try:
        #     cur.execute(sql,lis)
        # except Exception,e:
        #          print ("insert Error...",e)
        #     con.rollback()
        # else:
        #     con.commit()
        cur.close()
        con.close()

        return item
