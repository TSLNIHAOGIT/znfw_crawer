from scrapy import Spider,Request
import  urllib
# from douban.items import DoubanItem
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class SanzhaSpider(Spider):
  name = "douban"
  # allowed_domains = ["http://www.douban.com"]
  start_urls = ('https://www.douban.com/?p=20',)
  # page=1
  cookie=settings['COOKIE']
  headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
      'Accept-Encoding': 'gzip, deflate,br',
      'Accept-Language': 'zh-CN,zh;q=0.8',
      'Connection': 'keep-alive',  # 保持链接状态
      'Referer': 'https://www.douban.com/',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
  }  # 这是请求头，用来伪装成浏览器行为
  meta = {
      'dont_redirect': True,  # 禁止网页重定向
      'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
  }
  # print('cookie',cookie)
  def start_requests(self):
      # print(self.start_urls[0])
      # print(self.headers)
      yield Request(self.start_urls[0],
                    cookies=self.cookie,
                    headers=self.headers,
                    meta=self.meta,
                    callback=self.parse)

  def parse(self, response):
      response_url = response.url
      query = urllib.parse.urlparse(response_url).query
      # print('query', query)
      params = urllib.parse.parse_qs(query)
      # print('params', params)
      page = params['p'][0]
      # print('page', page)
      print("*****************\n", '第%s页' % (page), response_url)

      name = response.xpath('//div[@class="text"]/a/text()').extract()
      uri_list=response.xpath('//div[@class="text"]/a/@href').extract()
      print('name', name)
      # print("uri_list", uri_list)
      for uri in uri_list:
          print('uri',uri)
          yield Request(uri,
                    cookies=self.cookie,
                    headers=self.headers,
                    meta=self.meta,
                    callback=self.parse_item)

      uri_page='https://www.douban.com/'
      page = int(page) + 1
      url=uri_page + '?p=%s' %(page)

      yield Request( url,
                    cookies=self.cookie,
                    headers=self.headers,
                    meta=self.meta,
                    callback=self.parse)

      #写到文件中，看是否登录成功
      with open('login.html', 'wb') as file:
          file.write(response.body)
          file.close()


  def parse_item(self,response):
      note=response.xpath('//div[@class="note-header pl2"]/a/text()').extract()
      print('note',note)
      # print('body',response.body)

