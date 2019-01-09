import scrapy
import  urllib
import re
from scrapy.loader import ItemLoader
from scrapy.exceptions import CloseSpider
# class DmozSpider(scrapy.Spider):
#     name = "dmoz"
#     allowed_domains = ["dmoz.org",'lihun66.com']
#     start_urls = [


#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
#         "http://www.lihun66.com/ask/browser.php?tid2=2&page=1"
#     ]
#
#     def parse(self, response):
#         filename = response.url.split("/")[-2]
#         with open(filename, 'wb') as f:
#             f.write(response.body)

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):

    name = "lihun"
    # allowed_domains = ["dmoz.org",'lihun66.com']
    '''Scrapy为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，并将 parse 方法作为回调函数(callback)赋值给了Request'''
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        "http://www.yifatong.com/ask/lihunzixun/p1.html"
    ]
    '''Request对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法'''
    '''parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。 
    该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象'''
    # def parse(self, response):
    #     print('***********response:',type(response),response.body)
    #     for sel in response.xpath('//ul/li'):
    #         item = DmozItem() #Item 对象是自定义的python字典。 您可以使用标准的字典语法来获取到其每个字段的值。(字段即是我们之前用Field赋值的属性
    #         item['title'] = sel.xpath('a/text()').extract()
    #         item['link'] = sel.xpath('a/@href').extract()
    #         item['desc'] = sel.xpath('text()').extract()
    #         yield item      #yield是一个关键词，类似return, 不同之处在于，yield返回的是一个生成器,Spider将会将爬取到的数据以 Item 对象返回
    def __init__(self):
        self.page=1
    def parse(self, response):
       # uri_list=response.xpath('//div[@class="list-block h100p o-h"]//dd//a/@href').extract()
       uri_list = response.xpath('//ul[@class="list-unstyled"]/li/p//a[2]/@href').extract()#加入h4出错
       print('页面链接数为：',len(uri_list))
       response_url=response.url
       print('response_url\n',response_url)
       for uri in uri_list:
            uri_1 = 'http://www.yifatong.com' + uri
            # print(uri_1)
            if self.page<10:
                yield response.follow(url=uri_1, callback=self.parse_item_1)
            elif self.page<163:
                yield response.follow(url=uri_1, callback=self.parse_item_2)
            else:
                yield response.follow(url=uri_1, callback=self.parse_item_3)
       # uri_2 = response_url.replace('&page=%s' % page, '')
       self.page = self.page + 1
       uri_2="http://www.yifatong.com/ask/lihunzixun/p%s.html" %(self.page)

       # item = DmozItem()  # 在item.py中定义好的，该字典将会被返回给pipeline调用**********
       # item['type'] = '%s' %page   # ***********
       # yield item

       if self.page>269:
           print('哈哈哈哈哈')
           raise CloseSpider()
       yield scrapy.Request(url=uri_2, callback=self.parse)
    def parse_item_1(self, response):
        # with open(r'/Users/ozintel/Tsl_exercise/znfw_crawer/tutorial2/data/law.html','wb') as f:
        #     body=response.body
        #     print(body)
        #     f.write(body)
        item=DmozItem()#在item.py中定义好的，该字典将会被返回给pipeline调用
        item['web_category'] =''.join(response.xpath('//div[@class="lvshijieda-body"]//p//span[last()]/a/text()').extract())
        item['text'] =''.join(response.xpath('//div[@class="jieda-weijieda"]/div[@class="jd-wjd-wenti"]//p[1]/text()').extract())
        title=''.join(response.xpath('//div[@class="jieda-weijieda"]//h2/text()').extract())
        item['title']=re.sub('\s','',title)
        answer=''.join(response.xpath('//div[@class="jd-yjd-wenti"]//p/text()').extract())
        item['answer']=re.sub('\u3000\u3000|\r\n','',answer)
        # print('item',item)
        yield item

    def parse_item_2(self, response):
        # with open(r'/Users/ozintel/Tsl_exercise/znfw_crawer/tutorial2/data/law.html','wb') as f:
        #     body=response.body
        #     print(body)
        #     f.write(body)
        item = DmozItem()  # 在item.py中定义好的，该字典将会被返回给pipeline调用
        item['web_category'] = ''.join(
            response.xpath('//div[@class="lvshijieda-body"]//p//span[last()]/a/text()').extract())

        item['text'] = ''.join(
            response.xpath('//div[@class="anwser-bar p-r"]//span[@class="w4 lh2"]/text()').extract())
        title = ''.join(response.xpath('//div[@class="jieda-index-mod"]//div[@class="r-bar"]/p/text()').extract())
        item['title'] = re.sub('\s', '', title)
        answer = ''.join(response.xpath('//div[@class="question-part p-r"]//span[@class="w4"]/p/text()').extract())
        item['answer'] = re.sub('\u3000\u3000|\r\n', '', answer)
        # print('item',item)
        yield item
    def parse_item_3(self, response):
        # with open(r'/Users/ozintel/Tsl_exercise/znfw_crawer/tutorial2/data/law.html','wb') as f:
        #     body=response.body
        #     print(body)
        #     f.write(body)
        item = DmozItem()  # 在item.py中定义好的，该字典将会被返回给pipeline调用
        item['web_category'] = ''.join(
            response.xpath('//div[@class="lvshijieda-body"]//p//span[last()]/a/text()').extract())

        item['text'] = ''.join(
            response.xpath('//div[@class="anwser-bar p-r"]//span[@class="w4 lh2"]/text()').extract())
        title = ''.join(response.xpath('//div[@class="jieda-index-mod"]//div[@class="r-bar"]/p/text()').extract())
        item['title'] = re.sub('\s', '', title)
        answer = ''.join(response.xpath('//div[@class="question-part p-r"]//span[@class="w4"]/text()').extract())
        item['answer'] = re.sub('\u3000\u3000|\r\n', '', answer)
        # print('item',item)
        yield item

    def parse_item2(self,response):
        l = ItemLoader(item=DmozItem(), response=response)
        l.add_xpath('type','//div[@class="location ask_main_location"]/span[@class="fl"]/a[last()]/text()')
        l.add_xpath('type','//div[@class="question"]/h2/text()')
        l.add_xpath('answer','//div[@class="anwser"]/h2/text()')
        l.add_value('answer','牛逼')
        yield l.load_item()





'''
parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。 
该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象

Scrapy为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，并将 parse 方法作为回调函数(callback)赋值给了Request。
Request对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法。


'''