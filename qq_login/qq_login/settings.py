# -*- coding: utf-8 -*-

# Scrapy settings for qq_login project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qq_login'

SPIDER_MODULES = ['qq_login.spiders']
NEWSPIDER_MODULE = 'qq_login.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qq_login (+http://www.yourdomain.com)'

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
#    'qq_login.middlewares.QqLoginSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'qq_login.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'qq_login.pipelines.QqLoginPipeline': 300,
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

# COOKIE = {'RK': 'u99D18A/Gn', 'pgv_pvi': '8834054144', 'pgv_si': 's3516455936', '_ga': 'GA1.2.731358157.1509695790', '_gid': 'GA1.2.1172141046.1509695790', 'pgv_info': 'ssid', 'pgv_pvid': '8082356376', 'Loading': 'Yes', 'qz_screen': '1440x900', 'QZ_FE_WEBP_SUPPORT': '1', 'cpu_performance_v8': '1', '_qz_referrer': 'i.qq.com', 'ptui_loginuin': '1330065671', 'ptisp': 'ctc', 'ptcz': '84e85d841a7b24e4b073fb161145f2cf1f85f8a4384480c4917b5dcffb71f72e', 'uin': 'o1330065671', 'skey': '@lDQdZFJcw', 'pt2gguin': 'o1330065671', 'p_uin': 'o1330065671', 'pt4_token': '87qE5pu7bUSmhrDJLNg6cspYsUUv7A1TGaLZBhzzId4_', 'p_skey': 'Foi327P64TMi-Z6-82nhVdFuQ3e8oOTiVrbEO31gDSY_'}
# COOKIE = {
#     'RK': 'u99D18A/Gn',
#     'pgv_pvi': '8834054144',
#     'pgv_si': 's3516455936',
#     '_ga': 'GA1.2.731358157.1509695790',
#     '_gid': 'GA1.2.1172141046.1509695790',
#     'pgv_info': 'ssid', 'pgv_pvid': '8082356376',
#     'QZ_FE_WEBP_SUPPORT': '1',
#     'cpu_performance_v8': '1',
#     'Loading': 'Yes',
#     'qz_screen': '1440x900',
#     '__Q_w_s__QZN_TodoMsgCnt': '1',
#     '_qz_referrer': 'i.qq.com',
#     'ptui_loginuin': '1330065671',
#     'ptisp': 'ctc',
#     'ptcz': '84e85d841a7b24e4b073fb161145f2cf1f85f8a4384480c4917b5dcffb71f72e',
#     'uin': 'o1330065671',
#     'skey': '@vSED86lZo',
#     'pt2gguin': 'o1330065671',
#     'p_uin': 'o1330065671',
#     'pt4_token': 'n7GPy3Kz5zzYPDLYpOn11BvnAj6-hHdzQUl0iAsuRoU_',
#     'p_skey': 'F1yHluJj*Ftn54seMvB3zjqBxKx942Mra0hRCvh*8Bs_'}
COOKIE={'RK': 'u99D18A/Gn', 'pgv_pvi': '8834054144', '_ga': 'GA1.2.731358157.1509695790', 'pgv_pvid': '8082356376', '__Q_w_s__QZN_TodoMsgCnt': '1', 'pgv_info': 'ssid', 'pgv_si': 's6636962816', 'qqmusic_uin': '', 'qqmusic_key': '', 'qqmusic_fromtag': '', 'qzmusicplayer': 'qzone_player_1029439477_1509849983398', 'rv2': '800FC8920FF277C94D498A265F02FED22C78B22D450CFD5390', 'property20': '0FE1A502801E15B1F57C4590FBE6B5F15252AEF996E6BDDA1F8BEEF7DFAE560F0B4B00834B12FCFF', 'zzpaneluin': '', 'zzpanelkey': '', 'Loading': 'Yes', 'qz_screen': '1440x900', 'QZ_FE_WEBP_SUPPORT': '1', 'cpu_performance_v8': '1', '_qz_referrer': 'i.qq.com', 'ptui_loginuin': '1330065671', 'ptisp': 'ctc', 'ptcz': '84e85d841a7b24e4b073fb161145f2cf1f85f8a4384480c4917b5dcffb71f72e', 'uin': 'o1330065671', 'skey': '@E8tE9qBUj', 'pt2gguin': 'o1330065671', 'p_uin': 'o1330065671', 'pt4_token': 'zam1h42WKwv9LR32Fmk1gyEiUsJqIpQqokvmUVNuLO0_', 'p_skey': '9nmBHNRknFQPcfyhxzi4SKbrUTnPrOR3Xds24t0SWiI_'}
