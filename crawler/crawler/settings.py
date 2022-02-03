BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'


# JOBDIR = 'crawls/torspider-1'
DEPTH_LIMIT = 1

CONCURRENT_REQUESTS = 8
DOWNLOAD_DELAY = 0.25
#CONCURRENT_REQUESTS_PER_IP = 16
REACTOR_THREADPOOL_MAXSIZE = 20
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 240
REDIRECT_ENABLED = False
DEPTH_PRIORITY = 1
SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

#SPIDER_MIDDLEWARES = {
#    'crawler.middlewares.CrawlerSpiderMiddleware': 543,
#}

DOWNLOADER_MIDDLEWARES = {
   'crawler.middlewares.ProxyMiddleware': 100,
}

#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

#ITEM_PIPELINES = {
#    'crawler.pipelines.CrawlerPipeline': 300,
#}

#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False

