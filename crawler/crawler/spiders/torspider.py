import scrapy

class TorSpider(scrapy.Spider):
    name = 'torspider'
    start_urls = ['http://torcatalog.com']

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            # yield response.follow(next_page, self.parse)
            if link.startswith('http') and '.onion' in link:
                yield { 'link': link }
