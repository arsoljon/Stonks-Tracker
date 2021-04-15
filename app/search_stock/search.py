from .stock_request import Stock_request as req
from .find_stock import Find_stock as find
from .save_stock import Save_stock as save
import os

class Search():
    __url = ""
    def __set_url(self): self.__url = "https://finance.yahoo.com/quote/"

    def __init__(self, t):
        self.__set_url()
        req(t,self.get_url())
        find()
        save()

    def get_url(self): return self.__url


