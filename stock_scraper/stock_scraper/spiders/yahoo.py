import scrapy


class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['http://finance.yahoo.com/']

    def parse(self, response):
        pass
