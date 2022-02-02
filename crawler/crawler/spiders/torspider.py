import time
import scrapy

from crawler.items import CrawlerItem

class TorSpider(scrapy.Spider):
    name = 'torspider'
    start_urls = ['http://torcatalog.com']

    def parse(self, response):
        item = CrawlerItem()
        item['link'] = response.url
        item['last_updated'] = time.time()
        item['title'] = response.css('title::text').get()
        item['description'] = response.css('meta[name=description]::attr(content)').get()
        item['keywords'] = ', '.join(response.css('meta[name=keywords]::attr(content), h1::text, h2::text, h3::text, b::text, strong::text').getall())
        item['text'] = ' '.join(response.css('body *::text').getall())
        yield item

        for link in response.css('a::attr(href)').getall():
            if link.startswith('http') and '.onion' in link:
                yield response.follow(link, self.parse)
