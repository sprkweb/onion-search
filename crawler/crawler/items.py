from dataclasses import dataclass
import scrapy

class CrawlerItem(scrapy.Item):
    link = scrapy.Field()
    last_updated = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    keywords = scrapy.Field()
    text = scrapy.Field()
