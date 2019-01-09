import scrapy
# import  urllib
import re
from scrapy.http import Request,FormRequest
from scrapy.loader import ItemLoader
from scrapy.exceptions import CloseSpider
from urllib import request
import  ssl
# import time
import os
print('kk',os.path.abspath('..'))
# print(os.path.abspath('.'))
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',  # 保持链接状态
        # 'Referer': 'https://www.douban.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }  # 这是请求头，用来伪装成浏览器行为

    name = "married_family_q"
    # allowed_domains = ["dmoz.org",'lihun66.com']
    '''Scrapy为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，并将 parse 方法作为回调函数(callback)赋值给了Request'''
    start_urls = [
        "http://www.lawtime.cn/ask/browse_s91_d201306.html"
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
        self.uri_2=''

    # def start_requests(self):
    #     """第一次请求一下登录页面，设置开启cookie使其得到cookie，设置回调函数"""
    #     #表示开启cookie记录，首次请求时写在Request()里
    #     return [Request(
    #         self.start_urls[0],
    #         headers=self.headers,
    #         callback=self.parse,
    #         meta={"cookiejar":1})]

#能用时start ,下面都有meta1



    def parse(self, response):
       response_status=response.status
       print('0状态码为：',response_status)
       response_url = response.url
       print('0.response_url:', response_url)


       if response_status==403:
           captcha = response.xpath("//img[@class='yzm-pic']/@src").extract()
           print('captcha', captcha)
           if len(captcha) > 0:
               # '''此时有验证码'''
               # 人工输入验证码
               print("正在保存验证码图片")

               captchapicfile = "/Users/ozintel/Tsl_exercise/znfw_crawer/lawtime_married_family/data／captcha.png"
               # urlopen = urllib.URLopener()
               # 下载图片流
               ssl._create_default_https_context = ssl._create_unverified_context

               with request.urlopen(captcha[0]) as fp:
                   data = fp.read()
                   # 清除并以二进制写入
                   f = open(captchapicfile, 'wb')
                   f.write(data)
                   f.close()

           print('开始写入response.body',response.body)
           with open(r'/Users/ozintel/Tsl_exercise/znfw_crawer/lawtime_married_family/data/A_1.html','wb') as f:
               f.write(response.body)

           # captcha = input('第%s次遇到验证码，请处理验证码:\n' % (self.state_count))
           # print('已经输入验证码，继续抓取：')
           #
           power_key  =''.join(response.xpath('//div[@class="regform-box"]/form[@name="reform"]/input[1]/@value').extract())
           captcha=input('*********captcha请输入验证码:\n')
           con_value=''.join(response.xpath('//div[@class="regform-box"]/form[@name="reform"]/input[2]/@value').extract())
           formdata={
           'vgcode': captcha,
           'power_key': power_key,
           # 'servertype': '10',
           # 'requestmode': 'async',
           'continue':con_value
           }
           print('formdata',formdata)
           self.state_count=self.state_count+1
           #分析源代码表单所得而不是network中看到的，那个不行
           # yield  FormRequest.from_response(response,
           #                            url='http://ipfilter.lsurl.cn/index.php?m=Home&c=IpFilter&a=submit_verification',
           #                            meta={"cookiejar": response.meta["cookiejar"]},
           #                            headers=self.headers,
           #                            formdata=formdata,
           #                            callback=self.parse_page,
           #                            )
           yield scrapy.FormRequest(
               url='http://ipfilter.lsurl.cn/index.php?m=Home&c=IpFilter&a=submit_verification',
               headers=self.headers,
               formdata=formdata,
               # callback=self.parse_page
               callback = self.parse
           )

           # time.sleep(5)
       else:

           # self.item_count = response.xpath('//div[@class="paging paging-a"]//span/text()').re('\d+')[0]
           # self.all = int(self.item_count) + self.all
           # print('********************', self.item_count, self.all)

           # uri_list=response.xpath('//div[@class="list-block h100p o-h"]//dd//a/@href').extract()


           #这个response总是有的
           uri_list = response.xpath('(//div[@class="paging paging-a"]/a/@href)[position()<last()]').extract()
           count_link=len(uri_list)
           print('每个网页中页码数为：',count_link)

           # if count_link==0 and response_status!=403:
           #     print('哈哈哈哈哈')
           #     raise CloseSpider()
           # if count_link!=0 or response_status==403:
           url_first=re.sub(r'http://www.lawtime.cn','',response_url)
           uri_list.append(url_first)
           for uri in uri_list:
                uri_1 ='http://www.lawtime.cn/'+uri
                # print(uri_1)
                yield response.follow(url=uri_1, callback=self.parse_item_1)

       self.month_1 = self.month_1 + 1
       if self.month_1 == 13:
           self.year_1 = self.year_1 + 1
           self.month_1 = 1
           m = '0' + str(self.month_1)
           ym=(self.year_1, m)
           # print(self.year_1, m)
       else:
           if self.month_1 <= 9:
               m = '0' + str(self.month_1)
               ym = (self.year_1, m)
               # print(self.year_1, m)
           else:
               ym = (self.year_1, self.month_1)
               # print(year_1, month_1)


       if self.year_1 == 2017 and self.month_1 > 11:
           raise CloseSpider()
           # print('ym',ym)
       uri_2="http://www.lawtime.cn/ask/browse_s91_d%s%s.html"  %ym
           # http: // www.lawtime.cn / ask / browse_s4_p13.html
           # uri_2="http://www.lawtime.cn/ask/browse_s4_p%s.html" %(self.page)
           # "http://www.lawtime.cn/ask/browse_s4_p1.html"

           # item = DmozItem()  # 在item.py中定义好的，该字典将会被返回给pipeline调用**********
           # item['type'] = '%s' %page   # ***********
           # yield item



       # yield scrapy.Request(url=uri_2,meta={"cookiejar":1}, callback=self.parse)
       yield scrapy.Request(url=uri_2, callback=self.parse)

        #每一页中提取所有的链接
    def parse_item_1(self, response):

        response_url = response.url
        print('1.response_url:', response_url)

        response_status = response.status
        print('1状态码为：', response_status)

        if response_status == 403:
            captcha = response.xpath("//img[@class='yzm-pic']/@src").extract()
            print('captcha', captcha)
            if len(captcha) > 0:
                # '''此时有验证码'''
                # 人工输入验证码
                print("正在保存验证码图片")

                captchapicfile = "/Users/ozintel/Tsl_exercise/znfw_crawer/lawtime_married_family/data／captcha1.png"
                # urlopen = urllib.URLopener()
                # 下载图片流
                ssl._create_default_https_context = ssl._create_unverified_context

                with request.urlopen(captcha[0]) as fp:
                    data = fp.read()
                    # 清除并以二进制写入
                    f = open(captchapicfile, 'wb')
                    f.write(data)
                    f.close()

            # captcha = input('第%s次遇到验证码，请处理验证码:\n' % (self.state_count))
            # print('已经输入验证码，继续抓取：')
            #
            power_key = ''.join(
                response.xpath('//div[@class="regform-box"]/form[@name="reform"]/input[1]/@value').extract())
            captcha = input('*********captcha请输入验证码:\n')
            con_value = ''.join(
                response.xpath('//div[@class="regform-box"]/form[@name="reform"]/input[2]/@value').extract())
            formdata = {
                'vgcode': captcha,
                'power_key': power_key,
                # 'servertype': '10',
                # 'requestmode': 'async',
                'continue': con_value
            }
            print('formdata', formdata)
            self.state_count = self.state_count + 1
            # 分析源代码表单所得而不是network中看到的，那个不行
            # yield  FormRequest.from_response(response,
            #                            url='http://ipfilter.lsurl.cn/index.php?m=Home&c=IpFilter&a=submit_verification',
            #                            meta={"cookiejar": response.meta["cookiejar"]},
            #                            headers=self.headers,
            #                            formdata=formdata,
            #                            callback=self.parse_page,
            #                            )
            yield scrapy.FormRequest(
                url='http://ipfilter.lsurl.cn/index.php?m=Home&c=IpFilter&a=submit_verification',
                headers=self.headers,
                formdata=formdata,
                # callback=self.parse_page
                callback=self.parse_item_1
            )


            # yield scrapy.FormRequest(
            #     url=url,
            #     formdata={"email": "xxx", "password": "xxxxx"},
            #     callback=self.parse_page
            # )
            # with open(r'/Users/ozintel/Tsl_exercise/znfw_crawer/lihun/data/law.html', 'wb') as f:
            #     f.write(response.body)
            # # very_code = input('第%s次遇到验证码，请处理验证码:\n' % (self.state_count))
            # print('已经输入验证码，继续抓取：')
        else:
            # with open(r'/Users/ozintel/Tsl_exercise/znfw_crawer/tutorial2/data/law.html','wb') as f:
            #     body=response.body
            #     print(body)
            #     f.write(body)
            item=DmozItem()#在item.py中定义好的，该字典将会被返回给pipeline调用
            links=response.xpath('//ul[@class="list-main"]/li/div/a/@href').extract()
            print('每一页中的内容数为：',len(links))
            for link in links:
                # print(link)
                yield response.follow(url=link, callback=self.parse_item_2)




    def parse_item_2_0(self,response):
        l = ItemLoader(item=DmozItem(), response=response)
        l.add_xpath('title','//div[@class="consult-question-contain"]/h1[@class="consult-question-title"]/text()')
        l.add_xpath('text','//div[@class="consult-question-contain"]/p[@class="consult-question-detail"]/text()')
        l.add_xpath('answer','//div[@class="consult-answer-detail"]//div[@class="consult-answer-detail-text"]/text()')
        # l.add_value('answer','牛逼')
        # print(l.load_item())
        yield l.load_item()
    def parse_item_2(self,response):

        response_url = response.url
        # print('2.response_url:', response_url)

        response_status = response.status
        print('2.response_url:', response_url,'\n','2状态码为：', response_status)

        if response_status == 403:
            self.state_count = self.state_count + 1
            # yield scrapy.FormRequest(
            #     url=url,
            #     formdata={"email": "xxx", "password": "xxxxx"},
            #     callback=self.parse_page
            # )
            # with open(r'/Users/ozintel/Tsl_exercise/znfw_crawer/lihun/data/law.html', 'wb') as f:
            #     f.write(response.body)
            # very_code = input('第%s次遇到验证码，请处理验证码:\n' % (self.state_count))
            # print('已经输入验证码，继续抓取：')
        else:
            item = DmozItem()  # 在item.py中定义好的，该字典将会被返回给pipeline调用
            item['title'] = ''.join(response.xpath('//div[@class="consult-question-contain"]/h1[@class="consult-question-title"]/text()').extract())
            # item['title'] = re.sub('\s', '', title)
            #
            item['text'] =''.join(response.xpath('//div[@class="consult-question-contain"]/p[@class="consult-question-detail"]/text()').extract())
            #
            answer=''.join(response.xpath('//div[@class="consult-answer-detail"]//div[@class="consult-answer-detail-text"]/text()').extract())
            item['answer']=re.sub('\u3000\u3000|\r\n','',answer)
            yield item
            # if item['text'] !='':
            #     yield item
    def parse_page(self,response):
        print('开始处理',response.body)
        with open(r'/Users/ozintel/Tsl_exercise/znfw_crawer/lawtime_married_family/data/page_403.html', 'wb') as f:
                f.write(response.body)
    # very_code = input('第%s次遇到验证码，请处理验证码:\n' % (self.state_count))
    # print('已经输入验证码，继续抓取：')




'''
parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。 
该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象

Scrapy为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，并将 parse 方法作为回调函数(callback)赋值给了Request。
Request对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法。


'''