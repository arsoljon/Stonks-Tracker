import pandas as pd
import os

class Find_stock():
    __raw_html = ""
    __ticker = ""
    __url = ""
    __previous_db = ""
    __new_db = ""

    def __retrieve_ticker_url_db(self):
        df = pd.read_csv(self.__get_previous_db(), sep=',', dtype=str)
        data = df.values.tolist()[0]
        self.__set_ticker(data[1])
        self.__set_url(data[2])

    def __launch_spider(self):
        os.chdir('stock_scraper')
        cmd = 'scrapy crawl yahoo'
        os.system(cmd)
        os.chdir('..')

    def __set_ticker(self, t): self.__ticker = t

    def __set_url(self, u): self.__url = u

    def __set_previous_db(self): self.__previous_db = "databases/ticker_url_db" #refactor to include a object of Stock_request and grab the db name from object.

    def __set_new_db(self): self.new_db = "databases/clean_stock_db"

    def __get_ticker(self):return self.__ticker

    def __get_url(self): return self.__url

    def __get_previous_db(self): return self.__previous_db

    def __get_new_db(self): return self.__new_db

    def __init__(self):
        self.__set_previous_db()
        self.__retrieve_ticker_url_db()
        self.__launch_spider()
