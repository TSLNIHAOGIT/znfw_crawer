import scrapy
import  urllib
import re
from scrapy.contrib.loader import ItemLoader
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
    name = "dmoz"
    allowed_domains = ["dmoz.org",'lihun66.com']
    '''Scrapy为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，并将 parse 方法作为回调函数(callback)赋值给了Request'''
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        "http://www.lihun66.com/ask/browser.php?tid2=2&page=1"
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
    def parse(self, response):
       uri_list=response.xpath('//div[@class="ask_main_l_m"]//a/@href').re(r'/ask.*')
       print('页面链接数为：',len(uri_list))
       response_url=response.url
       print('response_url',response_url)
       query = urllib.parse.urlparse(response_url).query
       params = urllib.parse.parse_qs(query)
       page = params['page'][0]
       for uri in uri_list:
            uri_1 = 'http://www.lihun66.com/' + uri
            print(uri_1)
            yield response.follow(url=uri_1, callback=self.parse_item)

       uri_2 = response_url.replace('&page=%s' % page, '')
       page = int(page) + 1

       item = DmozItem()  # 在item.py中定义好的，该字典将会被返回给pipeline调用**********
       item['type'] = '%s' %page   # ***********
       yield item

       if page>1966:
           print('哈哈哈哈哈')
           raise CloseSpider()
       yield scrapy.Request(url=uri_2 + '&page=%s' % page, callback=self.parse)


    def parse_item2(self,response):
        l = ItemLoader(item=DmozItem(), response=response)
        l.add_xpath('type','//div[@class="location ask_main_location"]/span[@class="fl"]/a[last()]/text()')
        l.add_xpath('type','//div[@class="question"]/h2/text()')
        l.add_xpath('answer','//div[@class="anwser"]/h2/text()')
        l.add_value('answer','牛逼')
        yield l.load_item()

    def parse_item(self, response):
        item=DmozItem()#在item.py中定义好的，该字典将会被返回给pipeline调用
        item['type'] = ''.join(response.xpath('//div[@class="location ask_main_location"]/span[@class="fl"]/a[last()]/text()').extract())
        content=''.join(response.xpath('//div[@class="question"]/text()').extract())
        item['content'] =re.sub(r'\r\n|\s+|\t','',content)
        item['title']=''.join(response.xpath('//div[@class="question"]/h2/text()').extract())
        answer=''.join(response.xpath('//div[@class="anwser"]/h2/text()').extract())
        item['answer'] = re.sub('\r\n|\u3000\u3000','',answer)
        print('item',item)
        # yield item




'''
parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。 
该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象

Scrapy为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，并将 parse 方法作为回调函数(callback)赋值给了Request。
Request对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法。


'''