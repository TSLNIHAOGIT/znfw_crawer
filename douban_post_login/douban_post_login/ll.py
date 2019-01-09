# def parse(self, response):
#          captcha=response.xpath('//*[@id="captcha_image"]/@src').extract()  #获取验证码图片的链接
#          print captcha
#          if len(captcha)>0:
#              '''此时有验证码'''
#              #人工输入验证码
#              #urllib.urlretrieve(captcha[0],filename="C:/Users/pujinxiao/Desktop/learn/douban20170405/douban/douban/spiders/captcha.png")
#              #captcha_value=raw_input('查看captcha.png,有验证码请输入:')
#
#              #用快若打码平台处理验证码--------验证码是任意长度字母，成功率较低
#              captcha_value=ruokuai.get_captcha(captcha[0])
#              reg=r'<Result>(.*?)</Result>'
#              reg=re.compile(reg)
#              captcha_value=re.findall(reg,captcha_value)[0]
#              print '验证码为：',captcha_value
#
#              data={
#                  "form_email": "weisuen007@163.com",
#                  "form_password": "weijc7789",
#                  "captcha-solution": captcha_value,
#                  #"redir": "https://www.douban.com/people/151968962/",      #设置需要转向的网址，由于我们需要爬取个人中心页，所以转向个人中心页
#              }
#          else:
#              '''此时没有验证码'''
#              print '无验证码'
#              data={
#                  "form_email": "weisuen007@163.com",
#                  "form_password": "weijc7789",
#                  #"redir": "https://www.douban.com/people/151968962/",
#              }
#          print '正在登陆中......'
#          ####FormRequest.from_response()进行登陆
#          return [
#              FormRequest.from_response(
#                  response,
#                  meta={"cookiejar":response.meta["cookiejar"]},
#                  headers=self.header,
#                  formdata=data,
#                  callback=self.get_content,
#              )
#          ]
#      def get_content(self,response):
#          title=response.xpath('//title/text()').extract()[0]
#          if u'登录豆瓣' in title:
#              print '登录失败，请重试！'
#          else:
#              print '登录成功'
#              '''
#              可以继续后续的爬取工作
#              '''
# 复制代码
# ruokaui.py代码如下：