# -*- coding: utf-8 -*-

# Scrapy settings for first project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'first'

SPIDER_MODULES = ['first.spiders']
NEWSPIDER_MODULE = 'first.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'first (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'first.middlewares.FirstSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'first.middlewares.FirstDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'first.pipelines.FirstPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
PROXIES = ['http://1.198.72.153:9999',
'http://1.198.72.39:9999','http://112.87.68.159:9999','http://112.87.71.22:9999',
'http://115.207.85.5:8118',
'http://117.85.163.89:8118','http://121.233.251.43:9999','http://122.137.16.181:8080',
'http://124.167.106.91:8118',
'http://163.204.243.80:9999',
'http://163.204.247.3:9999',
'http://180.139.123.52:8118',
'http://183.158.28.19:8118',
'http://60.13.42.128:9999',
'https://1.192.242.151:9999',
'https://1.197.16.111:9999',
'https://1.197.16.223:9999',
'https://1.197.203.126:9999',
'https://1.197.203.187:9999',
'https://1.198.72.104:9999',
'https://1.198.72.154:9999',
'https://1.198.73.254:9999',
'https://1.199.31.189:9999',
'https://110.189.152.86:52277',
'https://112.85.128.246:9999',
'https://112.85.129.195:9999',
'https://112.85.151.108:9999',
'https://112.85.164.140:9999',
'https://112.85.166.237:9999',
'https://112.85.169.78:9999',
'https://112.85.170.154:9999',
'https://112.85.170.239:9999',
'https://112.85.170.245:9999',
'https://112.85.171.213:9999',
'https://112.85.174.239:9999',
'https://112.87.131.160:8118',
'https://112.87.66.147:9999',
'https://112.87.68.124:9999',
'https://112.87.69.40:9999',
'https://112.87.69.48:9999',
'https://112.87.71.192:9999',
'https://112.87.71.248:9999',
'https://112.87.71.90:9999',
'https://113.108.242.36:47713',
'https://113.110.47.146:9999',
'https://113.121.20.133:9999',
'https://113.121.20.141:9999',
'https://113.121.20.20:27473',
'https://113.121.20.211:30584',
'https://113.121.23.137:9999',
'https://113.64.146.5:8118',
'https://114.230.69.170:9999',
'https://114.230.69.173:9999',
'https://114.230.69.60:9999',
'https://115.219.108.103:8010',
'https://115.221.127.171:808',
'https://117.84.218.29:8118',
'https://117.91.131.219:9999',
'https://117.91.232.177:9999',
'https://118.114.250.54:8118',
'https://119.254.94.114:45691',
'https://119.41.198.149:53281',
'https://120.83.104.66:9999',
'https://120.83.105.27:9999',
'https://120.83.108.57:9999',
'https://120.83.109.252:9999',
'https://120.83.110.215:9999',
'https://120.83.111.62:9999',
'https://121.233.251.218:9999',
'https://121.69.13.242:53281',
'https://122.193.246.218:9999',
'https://122.193.247.233:9999',
'https://123.163.96.107:9999',
'https://123.163.97.92:9999',
'https://123.169.35.109:9999',
'https://125.73.220.18:31036',
'https://163.204.240.26:9999',
'https://163.204.246.143:9999',
'https://163.204.246.242:9999',
'https://163.204.246.97:9999',
'https://163.204.247.186:9999',
'https://171.11.179.0:9999',
'https://171.11.179.248:9999',
'https://175.11.193.182:8118',
'https://175.148.79.177:1133',
'https://180.119.68.175:9999',
'https://180.119.68.42:9999',
'https://182.34.21.146:9999',
'https://183.63.101.62:53281',
'https://221.206.100.133:34073',
'https://222.89.32.142:48781',
'https://223.241.116.72:8010',
'https://27.154.34.146:31527',
'https://27.43.188.188:9999',
'https://27.43.190.116:9999',
'https://58.253.154.128:9999',
'https://58.253.155.69:9999',
'https://58.253.157.1:9999',
'https://58.253.158.182:9999',
'https://58.253.158.97:9999',
'https://58.253.159.198:9999',
'https://58.56.149.198:53281',
'https://58.58.213.55:8888',
'https://60.13.42.223:9999',
'https://60.13.42.52:9999',
'https://60.13.42.95:9999',
'https://118.24.0.108:8080','https://123.206.87.139:8888','https://171.80.113.104:9999','https://171.80.113.86:9999','https://171.80.114.47:9999']

