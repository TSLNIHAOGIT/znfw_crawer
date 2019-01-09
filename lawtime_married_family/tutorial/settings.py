# -*- coding: utf-8 -*-
import os
# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }


RETRY_HTTP_CODES = [500, 503, 504, 400, 404, 408]
RETRY_TIMES = 5





DOWNLOADER_MIDDLEWARES = {

    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    # 'tutorial.middlewares.CustomRetryMiddleware': 550,

    'tutorial.middlewares.RandomUserAgent': 500,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':600,
   # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':300,
   # 'tutorial.middlewares.MyproxiesSpiderMiddleware': 400,
}

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]


IPPOOL=[
    # {"ipaddr":"61.129.70.131:8080"},
    # {"ipaddr":"61.152.81.193:9100"},
    # {"ipaddr":"120.204.85.29:3128"},
    # {"ipaddr":"219.228.126.86:8123"},
    # {"ipaddr":"61.152.81.193:9100"},
    # {"ipaddr":"218.82.33.225:53853"},
    # {"ipaddr":"223.167.190.17:42789"},

    {"ipaddr":"59.40.68.84:8010"},
    {"ipaddr":"119.29.158.87:80"},
    {"ipaddr":"121.31.176.174:8123"},
    {"ipaddr":"61.135.217.7:80"},
    {"ipaddr":"59.40.50.63:8010"},
    {"ipaddr":"180.173.62.141:53281"},
    {"ipaddr":"111.155.116.206:8123"},
    {"ipaddr":"61.178.238.122:63000"},
    {"ipaddr":"121.238.137.252:8118"},
    {"ipaddr":"180.115.12.204:37940"},
    {"ipaddr":"49.85.0.123:24204"},
    {"ipaddr":"122.4.42.240:40587"},
    {"ipaddr":"120.33.247.130:43889"},
    {"ipaddr":"123.144.122.140:53281"},
    {"ipaddr":"114.246.72.83:8118"},
    {"ipaddr":"121.206.140.228:808"},
    {"ipaddr":"101.68.73.54:53281"},
    {"ipaddr":"110.73.49.125:8123"},
    {"ipaddr":"120.32.209.231:8118"},
    {"ipaddr":"110.73.29.30:8123"},
    {"ipaddr":"110.73.28.192:8123"},
    {"ipaddr":"59.40.51.100:8010"},
    {"ipaddr":"223.241.119.157:808"},
    {"ipaddr":"59.40.51.70:8010"},
    {"ipaddr":"222.85.50.239:808"},
    {"ipaddr":"125.86.58.160:80"},
    {"ipaddr":"1.194.130.18:808"},
    {"ipaddr":"223.241.116.113:8010"},
    {"ipaddr":"110.73.11.152:8123"},
    {"ipaddr":"180.118.241.73:808"},
    {"ipaddr":"183.184.113.20:8090"},
    {"ipaddr":"221.10.159.234:1337"},
    # {"ipaddr":"221.4.133.67:53281"},
    # {"ipaddr":"182.120.196.230:53281"},
    # {"ipaddr":"59.40.68.232:8010"},
    # {"ipaddr":"120.76.55.49:8088"},
    # {"ipaddr":"59.41.202.37:53281"},
    # {"ipaddr":"116.231.35.5:8118"},
    # {"ipaddr":"118.254.142.42:53281"},
    # {"ipaddr":"125.81.188.2:8123"},
    # {"ipaddr":"121.31.155.242:8123"},
    # {"ipaddr":"180.173.141.242:52335"},
    # {"ipaddr":"113.236.172.130:8118"},
    # {"ipaddr":"112.122.213.7:4392"},
    # {"ipaddr":"125.79.107.40:53281"},
    # {"ipaddr":"59.63.67.97:4362"},
    # {"ipaddr":"59.40.68.204:8010"},
    # {"ipaddr":"113.123.50.78:808"},
    # {"ipaddr":"111.76.67.74:4392"},
    # {"ipaddr":"171.212.140.116:8118"},
    # {"ipaddr":"175.171.108.227:53281"},
    # {"ipaddr":"180.122.148.227:23542"},
    # {"ipaddr":"123.96.138.24:21513"},
    # {"ipaddr":"59.40.69.237:8010"},
    # {"ipaddr":"59.63.74.160:4362"},
    # {"ipaddr":"59.34.201.30:808"},
    # {"ipaddr":"223.241.119.226:8010"},
    # {"ipaddr":"115.46.71.0:8123"},
    # {"ipaddr":"121.236.180.7:8118"},
    # {"ipaddr":"223.241.117.139:8010"},
    # {"ipaddr":"223.241.119.0:8010"},
    # {"ipaddr":"121.224.40.29:36684"},
    # {"ipaddr":"171.108.205.85:53281"},
    # {"ipaddr":"223.241.118.221:8010"},
    # {"ipaddr":"123.163.132.94:808"},
    # {"ipaddr":"124.89.33.59:53281"}

]

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

# '''分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内'''
ITEM_PIPELINES = {
    'tutorial.pipelines.TutorialPipeline':200,
   # 'tutorial.item_pipelines.PricePipeline': 100,
#    'tutorial.item_pipelines.JsonWriterPipeline': 200,
#    'tutorial.item_pipelines.DuplicatesPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 2
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# JOBDIR='./lawtime_married_family/data/jobdir_eg'

MONGO_HOST = "localhost"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "law"  # 库名
MONGO_USERNAME = "root"
MONGO_PASSWORD = "root"

LOG_LEVEL='INFO'

HTTPERROR_ALLOWED_CODES = [403]

# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

