from datetime import datetime, timezone
from scrapy.linkextractors import LinkExtractor
import scrapy

from crawler.items import CrawlerItem

class TorSpider(scrapy.Spider):
    name = 'torspider'
    start_urls = ['http://torcatalog.com']
    link_extractor = LinkExtractor(allow='.onion')

    def parse(self, response):
        item = CrawlerItem()
        item['link'] = response.url
        item['last_updated'] = datetime.now().astimezone(timezone.utc).isoformat()
        item['title'] = response.css('title::text').get()
        item['description'] = response.css('meta[name=description]::attr(content)').get()
        item['keywords'] = ', '.join(response.css('meta[name=keywords]::attr(content), h1::text, h2::text, h3::text, b::text, strong::text').getall())
        item['text'] = ' '.join(response.css('body *::text').getall())
        yield item

        for link in self.link_extractor.extract_links(response):
            yield scrapy.http.Request(link.url, callback=self.parse)
