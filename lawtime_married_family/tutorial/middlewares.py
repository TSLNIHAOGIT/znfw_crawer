# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class TutorialSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class RandomUserAgent(UserAgentMiddleware):
    def __init__(self, agents):
        self.agents = agents


    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        # print('agents:',self.agents)
        request.headers.setdefault('User-Agent', random.choice(self.agents))


# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html


from scrapy import signals
from tutorial.settings import IPPOOL
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class MyproxiesSpiderMiddleware(HttpProxyMiddleware):
    def __init__(self, ip=''):
        self.ip = ip
    def process_request(self, request, spider):
        thisip = random.choice(IPPOOL)
        # print("this is ip:" + thisip["ipaddr"])
        request.meta["proxy"] = "http://" + thisip["ipaddr"]



from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message

'''If Request.meta has dont_retry key set to True, the request will be ignored by this middleware.'''

class CustomRetryMiddleware(RetryMiddleware):

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        interval, redirect_url= get_meta_refresh(response)
        if redirect_url:
            print('redirect_url',redirect_url,'*******','response.url',response.url)

        # this is your check

        if response.status == 403 and response.url:
            print('*********************response.url',response.url)
            return self._retry(request, 'response got xpath "{}"'.format(response.url), spider) or response
        return response



# from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.response import get_meta_refresh
from scrapy import log

class CustomRetryMiddleware2(RetryMiddleware):

    def process_response(self, request, response, spider):
        url = response.url
        # if response.status in [301, 307]:
        if response.status in self.retry_http_codes:
            log.msg("trying to redirect us: %s" %url, level=log.INFO)
            reason = 'redirect %d' %response.status
            return self._retry(request, reason, spider) or response
        interval, redirect_url = get_meta_refresh(response)
        # handle meta redirect
        if redirect_url:
            log.msg("trying to redirect us: %s" %url, level=log.INFO)
            reason = 'meta'
            return self._retry(request, reason, spider) or response
        hxs = HtmlXPathSelector(response)
        # test for captcha page
        captcha = hxs.select(".//input[contains(@id, 'captchacharacters')]").extract()
        if captcha:
            log.msg("captcha page %s" %url, level=log.INFO)
            reason = 'capcha'
            return self._retry(request, reason, spider) or response
        return response