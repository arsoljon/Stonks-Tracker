import scrapy
import pandas as pd

class YahooSpider(scrapy.Spider):
    df_ticker = pd.read_csv('../databases/ticker_url_db', sep=',', dtype=str)
    ticker = df_ticker.to_dict()["Ticker"][0]
    site_loc = "quote/"

    name = 'yahoo'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['http://finance.yahoo.com/'+site_loc+ticker]

    def parse(self, response):
        price = response.xpath('//*[@class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"]/text()').extract()[0]
        data = {"Ticker": [self.ticker], "Current_price": [price]}
        df_data = pd.DataFrame(data, columns=["Ticker", "Current_price"])
        yield{df_data.to_csv("../databases/clean_stock_db", sep=',')}

