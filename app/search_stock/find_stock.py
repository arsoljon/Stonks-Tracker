#Run the yahoo spider on the most recent ticker.
import os

class Find_stock():
    def __launch_spider(self):
        os.chdir('stock_scraper')
        cmd = 'scrapy crawl yahoo'
        os.system(cmd)
        os.chdir('..')

    def __init__(self):
        self.__launch_spider()
