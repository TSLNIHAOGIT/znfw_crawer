# -*- coding: utf-8 -*-

# Scrapy settings for douban_login project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban_login'

SPIDER_MODULES = ['douban_login.spiders']
NEWSPIDER_MODULE = 'douban_login.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban_login (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douban_login.middlewares.DoubanLoginSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'douban_login.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'douban_login.pipelines.DoubanLoginPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


LOG_FILE="scrapy.log"

# COOKIE = {'ps': 'y',
#  '__utmz': '30149280.1480660612.10.6.utmcsr',
#  '这些就是登录页面之后在抓取的请求头中拷贝下来并按字典格式保存的cookies（部分删除）'
#    'll': '"118282"',
#   'ct': 'y'}

#登陆都是依据cookie进行的

COOKIE = {
    "JSESSIONID":"8149d535-ec66-4aab-835a-f006fe3ac5d4",
    "ll": "118318",
    "bid": "qhc4hCj3pxY",
    "__yadk_uid": "bZZUzu2somC0aomy1zMsJDuui2zBLrB7",
    "ps": "y",
    "_ga": "GA1.2.1240797434.1506605716",
    "_gid": "GA1.2.1170702336.1509673225",
    "ue": "1330065671@qq.com",
    # _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1509675449%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DyCzhW9NLUWuoef4To2Z_wHO7aOx5BqnrD7frlqLAZO3RXJBmEpfKugG_86mvCpZAQvyO2mcO73oGaU0HWkZ-yq%26wd%3D%26eqid%3Df4ed937e000010c30000000559ccfaac%22%5D;
    "push_noty_num": "0",
    "push_doumail_num": "0",
    "__utmt=1": "ap=1",
    "_vwo_uuid_v2":"9A70FCD7C85DF510FCBE2D6DD6EC3BAB|207ffacadfaf0824bd6d8075ca5016f1",
    "_pk_id.100001.8cb4":"4e67ebf48f2bc0d2.1506606101.4.1509680130.1509676001.",
    "_pk_ses.100001.8cb4":"*",
    "__utma":"30149280.1240797434.1506605716.1509675450.1509679624.6",
    "__utmb":"30149280.5.10.1509679624",
    "__utmc":"30149280",
    "__utmz":"""30149280.1509023920.2.2.utmcsr":"baidu|utmccn=(organic)|utmcmd=organic""",
     "__utmv":"30149280.16909",
    "dbcl2":"169093483:EfZ1pQ0EOWg"

}

