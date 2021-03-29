# https://finance.yahoo.com/quote/
# Combine url & ticker and make a csv file to save the data.
import requests
import pandas as pd

class Stock_request():
    __ticker = ""
    __url = ""
    __found = False

    def __set_ticker(self, t):
        self.__ticker = t

    def __set_url(self, u):
        if self.get_ticker() == "":
            print("Need a valid ticker.")
        else:
            self.__url = u + self.get_ticker()
            self.__set_found()

    def __set_found(self):
        if (requests.get(self.get_url())).status_code == 200:
            self.__found = True
        else:
            self.__ticker = ""
            self.__url = ""
            print("Error: Input a valid url")

    def __set_ticker_url_db(self):
        if self.get_found():
            data = {"Ticker": [self.get_ticker()], "URL": [self.get_url()]}
            df = pd.DataFrame(data, columns=["Ticker", "URL"])
            df.to_csv("ticker_url_db")

    def __init__(self, t, u):
        self.__set_ticker(t)
        self.__set_url(u)
        self.__set_found()
        self.__set_ticker_url_db()

    def get_ticker(self):
        return self.__ticker

    def get_url(self):
        return self.__url

    def get_found(self):
        return self.__found
