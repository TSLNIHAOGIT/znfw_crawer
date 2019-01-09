import scrapy
import  urllib
import re
from scrapy.loader import ItemLoader
from scrapy.exceptions import CloseSpider
import time
import os
print('kkk',os.path.abspath('..'))
print(os.path.abspath('.'))

#  /代表下级节点，／／代表下级多个节点， 同一级节点有很多个
class DmozSpider(scrapy.Spider):

    name = "test"
    # allowed_domains = ["dmoz.org",'lihun66.com']
    '''Scrapy为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，并将 parse 方法作为回调函数(callback)赋值给了Request'''
    start_urls = [
        # "http://www.baidu.com",
        'http://ipfilter.lsurl.cn/ipfilter/?continue=aHR0cDovL3d3dy5sYXd0aW1lLmNuL2Fzay9icm93c2VfczkxX2QyMDEzMDYuaHRtbA=='
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
        self.year_1=2013
        self.month_1=6
        self.state_count=0
        self.item_count=0
        self.all=0
    def parse(self, response):
       print(response.body)
       response_status=response.status
       print('0状态码为：',response_status)
       response_url = response.url
       print('0.response_url:', response_url)


       power_key =''.join(response.xpath('//div[@class="regform-box"]/form[@name="reform"]/input[1]/@value').extract())
       captcha = ''

       formdata={
       'captcha': captcha,
       'power_key': power_key,
       'servertype': 10,
       'requestmode': 'async'
       }
       print('formdata',formdata)
       self.state_count=self.state_count+1
       # yield scrapy.FormRequest(
       #     url=response_url,
       #     formdata=formdata,
       #     callback=self.parse_page
       # )
       with open(r'/Users/ozintel/Tsl_exercise/znfw_crawer/test_spider/test_spider/data/test.html','wb') as f:
           f.write(response.body)
       # very_code = input('第%s次遇到验证码，请处理验证码:\n' % (self.state_count))
       print('已经输入验证码，继续抓取：')
