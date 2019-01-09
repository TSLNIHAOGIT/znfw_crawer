from scrapy import Spider,Request
import  urllib
# from douban.items import DoubanItem
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class SanzhaSpider(Spider):
  name = "qq_spider"
  # allowed_domains = ["http://www.douban.com"]
  start_urls = (
                # 'https://qzone.qq.com',
                # 'https://i.qq.com/',
                  'https://user.qzone.qq.com/1330065671',
                 # 'https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?uin=1330065671&do=1&rd=0.3559664419040802&fupdate=1&clean=1&g_tk=2014143248&qzonetoken=74c1ace4325e067b6782a6d20d032e717a29ac3f2b99f802c025541abe9b8aa10ee066f348ff8e0c50e2&g_tk=2014143248'
#链接和cookie要对应
                )
  # page=1
  cookie=settings['COOKIE']

  headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
      'Accept-Encoding': 'gzip, deflate,br',
      'Accept-Language': 'zh-CN,zh;q=0.8',
      'Connection': 'keep-alive',  # 保持链接状态
      'Referer': 'https://qzs.qzone.qq.com/qzone/v5/loginsucc.html?para=izone&from=iqq',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
  }  # 这是请求头，用来伪装成浏览器行为
  meta = {
      'dont_redirect': True,  # 禁止网页重定向
      'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
  }
  print('cookie',cookie)
  def start_requests(self):
      # print(self.start_urls[0])
      # print(self.headers)
      yield Request(self.start_urls[0],
                    cookies=self.cookie,
                    headers=self.headers,
                    meta=self.meta,
                    callback=self.parse)


  def parse(self,response):

      # name=response.xpath('//div[@class="f-nick"]/a/text()').extract()
      # print('name',name)
      url='https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?uin=1330065671&do=1&rd=0.7009992448640003&fupdate=1&clean=1&g_tk=470876335&qzonetoken=6568171003da1b6770daf60877c135862bba8f1cce835ceb22b6b724c4ae8eba1c03bf7b27c6ad691e5f&g_tk=470876335'
      yield Request(url,
                    cookies=self.cookie,
                    headers=self.headers,
                    meta=self.meta,
                    callback=self.parse_item)
  def parse_item(self,response):

      # print('开始处理body')
      # # 写到文件中，看是否登录成功
      with open('login.html', 'wb') as file:

          file.write(response.body)
      # response_url = response.url
      # query = urllib.parse.urlparse(response_url).query
      # # print('query', query)
      # params = urllib.parse.parse_qs(query)
      # # print('params', params)
      # page = params['p'][0]
      # # print('page', page)
      # print("*****************\n", '第%s页' % (page), response_url)
      #
      # name = response.xpath('//div[@class="text"]/a/text()').extract()
      # uri_list=response.xpath('//div[@class="text"]/a/@href').extract()
      # print('name', name)
      # print("uri_list", uri_list)
      # for uri in uri_list:
      #     print('uri',uri)
      #     yield Request(uri,
      #               cookies=self.cookie,
      #               headers=self.headers,
      #               meta=self.meta,
      #               callback=self.parse_item)

      # uri_page='https://www.douban.com/'
      # page = int(page) + 1
      # url=uri_page + '?p=%s' %(page)
      #
      # yield Request( url,
      #               cookies=self.cookie,
      #               headers=self.headers,
      #               meta=self.meta,
      #               callback=self.parse)





  # def parse_item(self,response):
  #     note=response.xpath('//div[@class="note-header pl2"]/a/text()').extract()
  #     print('note',note)
  #     # print('body',response.body)

