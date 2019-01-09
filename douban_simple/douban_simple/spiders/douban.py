##-*-coding:utf-8 -*-
import scrapy
from douban_simple.items import DoubanItem #将先前在items类中定义的“变量”引入进来
# from scrapy.conf import settings #用于引入settings中的内容，在使用cookies时候会用到
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

class DoubanMovieSpider(scrapy.Spider): #建立继承spider类的类
    name = 'douban' #这是爬虫的名字，是唯一的
    # allowed_domains = ['douban.com'] #规定爬虫爬去的域
    start_urls = (
        'https://movie.douban.com/chart',
        # 'http://www.lihun66.com',
                ) #设置爬虫爬取的初始链接
    cookie = settings['COOKIE'] #这里取得settings中定义的变量COOKIE的值，也就是登录网页时request headers中的cookies信息
    headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive', # 保持链接状态
    'Referer':'https://accounts.douban.com/login?alias=*******略',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    } #这是请求头，用来伪装成浏览器行为
    meta = {
    'dont_redirect':True, # 禁止网页重定向
    'handle_httpstatus_list':[301,302] # 对哪些异常返回进行处理
    }

    #start_requests方法返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request,该方法的默认实现是使用 start_urls 的url生成Request。
    def start_requests(self):
        print('self.start_urls[0]',self.start_urls[0])
        yield scrapy.Request(self.start_urls[0],callback=self.parse,cookies=self.cookie,headers=self.headers,meta=self.meta)

    def parse(self,response): #scrapy 默认的第一个解析函数，如果未在start_requests中指定其他回调函数的话
        # content=response.xpath('//title/text()').extract()
        # movie=response.xpath('//div[@class="pl2"]/a/text()').extract()
        # print('title',content)
        # print('movie',movie)
        print(str(response.body))
        print (response.url)
        with open('test.html','wb') as f: #调试的时候下载获取的网页以确认是否登录到指定页面
            f.write(response.body)
        #通过xpath获取想要的信息，个人喜欢xpath，C写的，比较快
        tables = response.xpath('//div[@class="indent"]/div/table')
        print('tables',tables.extract())
        items = []
        for table in tables:
            item = DoubanItem()
            item['movie_url'] = table.xpath('tr[1]/td[2]/div[@class="pl2"]/a/@href')[0].extract() #电影链接
            name1 = table.xpath('tr[1]/td[2]/div[@class="pl2"]/a/text()')[0].extract().strip().split('/')[0].strip()
            name2 = table.xpath('tr[1]/td[2]/div[@class="pl2"]/a/span/text()')[0].extract().strip()
            name =  name1+' / '+name2 #电影名称
            item['movie_name'] = name
            item['movie_star'] = table.xpath('tr[1]/td[2]/div[@class="pl2"]/div/span[@class="rating_nums"]/text()')[0].extract()
            items.append(item)
            print('name1',name1)
            print('name2', name2)
            print('name', name)
        print (u'爬取完毕...')
        return items #爬取完毕之后scrapy会自动执行pipeline的内容

